'''
The API daily rate limit for checking IP/Domains is 1,000. Upon reaching the daily limit
A HTTP 429 Too Many Request status will be returned.

By default, you receive an entire HTML page, which is why you should set "Accept: application/json"
when working with the API programmatically.

# How AbuseIPDB retrieves its IP details #
AbuseIPDB retrieves its Geolocation, usafe type, ISP and domain name from a paid service provider called IP2Location
https://www.ip2location.com/database/ip2location

# Request Parameters #
ipAddress: Required = Yes
maxAgeInDays: Required = No, Default: 30, min 1, max 365. This is how far back to fetch reports.
verbose: Required = No. This field will include reports within the response.

The endpoint accepts a single IP address (v4 or v6).
he desired data is stored in the data property. Here you can inspect details regarding the IP
address queried, such as version, country of origin, usage type, ISP, and domain name.
Also, there is the abusive reports.

The IP address should be url-encoded, because IPv6 addresses use colons, which are reserved
characters in URIs.

Full information: https://docs.abuseipdb.com/#check-endpoint
'''

import requests
import json

from osint.api.comms import HTTP_HEADER
from osint.api.comms import HTTP
from osint.api.osint import Osint
import osint.api.utils as utils
import osint.api.paths as paths
import requests

import logging
log = logging.getLogger(__name__)

class AbuseIPDB(Osint):

    _max_days = 365
    _min_days = 1


    class Report():
        def __init__(self, date="", comment=""):
            self.data = date
            self.comment = comment

    def __init__(self):
        self.initialise_url('https://api.abuseipdb.com/api/v2/check')
        self.initialise_api_key("abuseipdb")
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

    def check_ip(self, ip, days=30):
        headers = super().headers
        headers.accept_json()
        headers.set_custom('Key', self.API_KEY)

        http = super().http

        params = {'ipAddress': ip, 'maxAgeInDays': days, 'verbose':''}
        for key, value in params.items():
            http.param(key, value)
        response = requests.request(method=HTTP.method_get(), url=self.URL, headers=headers.headers, params=http.params)
        self.parse_results(response)
        return self

    def parse_results(self, response):
        json_obj = response.json()
        data = json_obj['data']

        self.ip = data['ipAddress']
        self.is_public = data['isPublic']
        self.abuse_score = data['abuseConfidenceScore']
        self.country = data['countryCode']
        self.country_name = data['countryName']
        self.usage_type = data['usageType']
        self.isp = data['isp']
        self.domain = data['domain']
        self.total_reports = data['totalReports']
        self.last_report_date = data['lastReportedAt']

        for report in data['reports']:
            self.reports.append(Report(date=report['reportedAt'], comment=report['comment'], categories_ids=report['categories']))

    def get_website_url(self, ioctype=None, ioc=""):
        return f'www.abuseipdb.com/check/{ioc}'

    def MAX_DAYS(self):
        return 365

    def MIN_DAYS(self):
        return 1

    def get_formatted_results(self, ip=False, isPublic=False, abuse_score=False, country=False, country_name=False,
                              usage_type=False, isp=False, domain=False, total_reports=False, last_report_date=False, all=False):
        pass





def initialise_report_categories():
    content = utils.get_file_contents(paths.abuseip_categories)
    try:
        return json.loads(content)
    except Exception as e:
        print("Error loading the json data form the file: {0}".format(paths.abuseip_categories))


class Report:
    _report_categories = initialise_report_categories()['abuseip_categories']

    def __init__(self, date="", comment="", categories_ids=[]):
        self.data = date
        self.comment = comment
        self.categories = self.parse_categories(categories_ids)

    def parse_categories(self, categories):
        log.info("Hello logging!")


        result_categories = []
        for category_id in categories:
            result_categories.append(Report._report_categories[str(category_id)])

        return result_categories


