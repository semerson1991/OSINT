import api.utils as utils
import api.comms as comms
import requests as requests
from api.osint import Osint


class VirusTotal(Osint):
    def __init__(self):
        self.initialise_url("https://www.virustotal.com/vtapi/v2/")
        self.initialise_api_key("virus_total")

        self.ip = None
        self.verbose_msg = None
        self.asn = None
        self.country = None
        self.resolutions = None

        self.detected_urls = None
        self.detected_downloaded_samples = None
        self.detected_communicating_samples = None
        self.detected_referrer_samples = None

        self.undetected_urls = None
        self.undetected_download_samples = None
        self.undetected_communicating_samples = None
        self.undetected_downloaded_samples = None
        self.undetected_referrer_samples = None

    def parse_results(self, data):
        self.verbose_msg = data.get('verbose_msg')
        self.asn = data.get('asn')
        self.country = data.get('country')

        if data.get('detected_communicating_samples'):
            self.detected_communicating_samples = len(data.get('detected_communicating_samples'))

        if data.get('detected_downloaded_samples'):
            self.detected_downloaded_samples = len(data.get('detected_downloaded_samples'))

        if data.get('detected_referrer_samples'):
            self.detected_referrer_samples = len(data.get('detected_referrer_samples'))

        if data.get('detected_urls'):
            self.detected_urls = len(data.get('detected_urls'))

        if data.get('resolutions'):
            self.resolutions = data.get('resolutions')

        if data.get('undetected_communicating_samples'):
            self.undetected_communicating_samples = len(data.get('undetected_communicating_samples'))

        if data.get('undetected_downloaded_samples'):
            self.undetected_downloaded_samples = len(data.get('undetected_downloaded_samples'))

        if data.get('undetected_referrer_samples'):
            self.undetected_referrer_samples = len(data.get('undetected_referrer_samples'))

    def check_domain(self, domain):
        pass

    @staticmethod
    def get_response_code_message(response_code):
        if response_code == 0:
            return "The item was not present in VirusTotal's dataset"
        if response_code == 1:
            return "The item was found and was successfully retrieved"
        if response_code == -2:
            return "The item is queued for analysis"

    @staticmethod
    def vt_request_limit_reached():
        utils.sleep("The VirusTotal request limit has been reached. The public API is limited to 4 requests per minute. \n"
              "  Sleeping for 30 seconds then retrying", 30)

    def check_ip(self, ip):
        self.ip = ip

        url = self.URL + "ip-address/report"
        print("Connecting ot Virus Total")
        params = {'apikey': self.API_KEY, 'ip': self.ip}
        response = requests.get(url, params=params, headers=comms.create_headers())

        if response.status_code == 204:
            self.vt_request_limit_reached()
        if response.status_code == 200:
            data = response.json()
            if data['response_code'] == 1:
                self.parse_results(data)
            else:
                print("The request was unsuccessful. Info {0}".format(data["verbose_msg"]))
        else:
            print("Request was unsuccessful - Status code: {0}".format(response.status_code))


def test():
    virus_total = VirusTotal()
    virus_total.check_ip("43.43.43.55")

    print('''
               Virustotal report for IP %s
               =======================
               ASN: %s
               Location: %s
               How many malicious samples communicated with this IP: %s
               How many malicious samples were downloaded from this IP: %s
                   ''' % (virus_total.ip, virus_total.asn, virus_total.country, virus_total.detected_communicating_samples, virus_total.detected_downloaded_samples))

test()