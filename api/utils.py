from time import sleep as time
import json


def get_file_contents(path):
    with open(path, 'r') as file:
        data = file.read()
        print(data)
    return data


def get_keys(path, key=""):
    contents = get_file_contents(path)
    try:
        keys = json.loads(contents)
        return keys['keys'][key]
    except Exception as e:
        print("An exception occured whilst trying to read the API key for: %s " % key)


def sleep(message, seconds):
    if message:
        print(message)
    time.sleep(seconds)





