

'''
in order to bypass internal User-Agent blacklist checks, it is recommended to provide a typical User-Agent string or the product name 'Falcon’

Quota per minute
Minute 0 / 200
Hour 0 / 2000

METHODS:
POST
/search/hash
summary for given hash

POST
/search/hashes
summary for given hashes

POST
/search/terms
'''

import requests
from osint.api.osint import Osint
from osint.api.comms import HTTP
import osint.api.utils as utils
import osint.api.paths as paths
import logging
log = logging.getLogger(__name__)


class HybridAnalysis(Osint):


    _max_requests_per_min = 200
    _max_requests_per_hour = 2000
    _base_url = "https://www.hybrid-analysis.com/api/v2"
    _hash_url = _base_url + "/search/hash"

    def __init__(self):
        self.initialise_url(self._base_url)
        self.initialise_api_key("hybrid-analysis")

    def check_hash(self, digest):
        self.failed_request = False
        headers = super().headers
        headers.accept_json()
        headers.set_user_agent("Falcon Sandbox")
        headers.set_custom('api-key', self.API_KEY)

        http = super().http

        params = {'hash': digest}
        for key, value in params.items():
            http.param(key, value)
        response = requests.post(
                                    url=self._hash_url,
                                    headers=headers.headers,
                                    data=http.params)
        if response.status_code == 200:
            return response.json() #If this returns empty, the hash has not been found in Hybrid Analysis database.
        else:
            response_text = response.text if response.text else ""
            log.info("Request failed with status code " + str(response.status_code) + " " + response_text)
            self.failed_request = True
            self.failed_text = response.text



    def parse_results(self, data):
        pass
    def get_website_url(self, ioctype=None):
        pass


class HybridAnalysisResult:

    def __init__(self):
        pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    log.setLevel(logging.DEBUG)

