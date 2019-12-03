import sys
import logging
import osint.api.paths as paths
import osint.api.utils as utils
from osint.api.comms import HTTP_HEADER
from osint.api.comms import HTTP


from abc import ABC, abstractmethod

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

try:
    import requests
except ImportError:
    print("\n  Required modules have not been found. \n"
          "  Please install them with:\n "
          "  pip install requests")
    sys.exit()


class Osint(ABC):
    headers = HTTP_HEADER()
    http = HTTP()

    URL = None
    API_KEY = None


    @abstractmethod
    def parse_results(self, data):
        pass

    @abstractmethod
    def get_formatted_results(self):
        pass

    @abstractmethod
    def get_website_url(self, ioctype=None):
        pass

    def initialise_url(self, url):
        self.URL = url

    def initialise_api_key(self, key=""):
        self.API_KEY = utils.get_keys(paths.api_key_dir + "keys", key)

        if self.API_KEY == "":
            print("No API key has been provided. Please add the api key to {0}".format(
                paths.api_key_dir + "keys"))

