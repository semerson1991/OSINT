" in order to bypass internal User-Agent blacklist checks, it is recommended to provide a typical User-Agent string or the product name 'Falcon’."

''' Quota per minute 
Minute 0 / 200
Hour 0 / 2000


'''

from osint.api.osint import Osint

import logging
log = logging.getLogger(__name__)


class HybriadAnalysis(Osint):


    _max_requests_per_min = 200
    _max_requests_per_hour = 2000
    _base_url = "www.hybrid-analysis.com/api/v2"
    _hash_url = _base_url + "\search/hash?"

    def __init__(self):
        super.__init__()
        self.initialise_url(self._base_url)
        self.initialise_api_key("hybrid-analysis")
        self.ip = ""
        self.is_public = ""
        self.abuse_score = ""
        self.country = ""
        self.country_name = ""
        self.usage_type = ""
        self.isp = ""
        self.domain = ""
        self.total_reports = ""
        self.last_report_date = ""
        self.reports = []

    def check_hash(self, hash):
        headers = super().headesr
        headers.accept_json()
        headers.set_useragent("Falcon Sandbox")

        http = super().http()
        params = {'hash': hash}
        for key, value in params.items():
            http.param(key, value)
        response = requests.request








if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    log.setLevel(logging.DEBUG)

