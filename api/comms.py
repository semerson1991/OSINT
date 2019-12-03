class HTTP:
    def __init__(self):
        self.params = {}
        pass

    def param(self, key, value):
        self.params[key] = value
        return self

    @staticmethod
    def method_get():
        return 'GET'

class HTTP_HEADER:

    def __init__(self):
        self.headers = {}

    def user_agent_mozilla(self):
        self.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"

    def set_user_agent(self, useragent):
        self.headers['User-Agent'] = useragent

    def accept_json(self):
        self.headers['Accept'] = 'application/json'

    def set_custom(self, key, value):
        self.headers[key] = value
