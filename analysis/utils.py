import json
def get_data(data_path):
    with open(data_path) as f:
        return json.load(f)

def get_file_with_postfix(files, p):
    return list(filter(lambda n: n[len(n) - len(p) :] == p, files))[0]