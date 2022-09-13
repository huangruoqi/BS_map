.PHONY: build shell start stop clean test black run
export PYTHONDONTWRITEBYTECODE=1
run:
	poetry run python ./analysis/main.py 

test:
	poetry run pytest ./test

black:
	poetry run black ./analysis/
	poetry run black ./test/



NAME=bs_map

GET_CONTAINER:=$(eval IS_CONTAINER=$(shell docker ps -a -f name=$$NAME | wc -l))
GET_STATUS:=$(eval IS_RUNNING=$(shell docker ps -f name=$$NAME | wc -l))

$(GET_CONTAINER) 
$(GET_STATUS) 

# if no container found
ifneq ($(IS_CONTAINER), 2)
start shell: build
else
build: clean
endif

# if container is running
ifeq ($(IS_RUNNING), 2)
clean: stop
else
shell: start
endif


build: 
	@docker build -t docker-practice .
	@docker run -dt --name $(NAME) docker-practice

shell:
	@docker exec -it $(NAME) bash
	@docker stop $(NAME)

start:
	@docker start $(NAME)

stop:
	@docker stop $(NAME)

ifeq ($(IS_CONTAINER), 2)
clean:
	@docker rm $(NAME)
endif