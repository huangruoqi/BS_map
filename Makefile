.PHONY: build shell start stop clean test black run
export PYTHONDONTWRITEBYTECODE=1


NAME=bs_map

GET_CONTAINER:=$(eval IS_CONTAINER=$(shell docker ps -a -f name=$$NAME | wc -l))
GET_STATUS:=$(eval IS_RUNNING=$(shell docker ps -f name=$$NAME | wc -l))

# if container is running
ifeq ($(IS_RUNNING), 2)
clean: stop
else
shell black run test: start 
endif

# if container found
ifeq ($(IS_CONTAINER), 2)
build: clean
clean:
	@docker rm $(NAME) > /dev/null
endif

start black run test: build
build: 
	@docker image rm bs_map_docker > /dev/null
	@docker build -t bs_map_docker . &> /dev/null
	@docker run -dt --name $(NAME) bs_map_docker > /dev/null

stop:
	@docker stop $(NAME) > /dev/null

shell:
	@docker exec -it $(NAME) bash

start:
	@docker start $(NAME) > /dev/null



run:
	@docker exec -it $(NAME) poetry run python ./analysis/main.py
	@make stop

test:
	@docker exec -it $(NAME) poetry run pytest ./test
	@make stop

black:
	@docker exec -it $(NAME) poetry run black ./analysis/
	@docker exec -it $(NAME) poetry run black ./test/
	@make stop
