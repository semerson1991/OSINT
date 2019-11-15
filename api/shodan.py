import api.utils as utils
import api.comms as comms
import requests as requests
from api.osint.osint import Osint

#Shodan API is limited to 1 request / second
class Shodan(Osint):
    def __init__(self):
        self.initialise_url("https://api.shodan.io")
        self.initialise_api_key("shodan")

        self.ip = None
        self.verbose_msg = None
        self.asn = None
        self.country = None
        self.resolutions = None

    def parse_results(self, data):
        pass

    def check_ip(self, ip):
        self.ip = ip
        url = self.URL + "/shodan/host/%s" % ip
        print("Connecting to Shodan.io")
        params = {'key': self.API_KEY}
        response = requests.get(url, params=params, headers=comms.create_headers())

        data = response.json()
        print (data)
        print (response.status_code)

def test():
    shodan = Shodan()
    shodan.check_ip("8.8.8.8")

test()