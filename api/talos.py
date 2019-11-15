from api.osint.osint import Osint
import api.comms as comms
import requests as requests


class Talos(Osint):

    def __init__(self):
        self.initialise_url("https://talosintelligence.com/sb_api/query_lookup/")

    def parse_results(self, data):
        pass

    def check_ip(self, ip):
        d = {"query": "/api/v2/details/ip/", "query_entry": ip, "offset": 0, "order": "ip asc"}
        r = requests.get("https://talosintelligence.com/sb_api/query_lookup/",
                         data=d, headers=comms.create_headers())

        print(r)
    def check_domain(self, ip):
        pass

#talos = Talos()
#talos.check_ip("8.8.8.8")
