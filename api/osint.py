import sys
import logging
import api.paths as paths
import api.utils as utils
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

    URL = None
    API_KEY = None


    @abstractmethod
    def parse_results(self, data):
        pass

    @abstractmethod
    def check_ip(self, ip):
        pass

    @abstractmethod
    def check_domain(self, ip):
        pass

    def initialise_url(self, url):
        self.URL = url

    def initialise_api_key(self, apikey_file):
        self.API_KEY = utils.get_file_contents(paths.api_key_dir + apikey_file)

        if self.API_KEY == "":
            print("No API key has been provided. Please add the api key to {0}".format(
                paths.api_key_dir + apikey_file))

