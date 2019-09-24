from time import sleep as time


def get_file_contents(path):
    with open(path, 'r') as file:
        data = file.read()
        print(data)
    return data


def sleep(message, seconds):
    if message:
        print(message)
    time.sleep(seconds)





