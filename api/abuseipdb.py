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

import json
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
    _daily_limit_reached = False
    
    type_ip = "IP"
    type_public_ip = "public_ip"
    type_abuse_score = "abusescore"
    type_country = "country"
    type_country_name = "country_name"
    type_usage_type = "usage_ype"
    type_isp = "isp"
    type_domain = "domain"
    type_total_reports = "total_reports"
    type_last_reported_date = "last_reported"

    def get_values(self, *value_types):

        values = {}
        for value_type in value_types:
            try:
                if value_type == self.type_ip:
                    values[value_type] = self._get_ipaddress()
                if value_type == self.type_public_ip:
                    values[value_type] = self._get_public_ip()
                if value_type == self.type_abuse_score:
                    values[value_type] = self._get_abuse_score()
                if value_type == self.type_country:
                    values[value_type] = self._get_country()
                if value_type == self.type_country_name:
                    values[value_type] = self._get_country_name()
                if value_type == self.type_usage_type:
                    values[value_type] = self._get_usage_type()
                if value_type == self.type_isp:
                    values[value_type] = self._get_isp()
                if value_type == self.type_domain:
                    values[value_type] = self._get_domain()
                if value_type == self.type_total_reports:
                    values[value_type] = self._get_total_reports()
                if value_type == self.type_last_reported_date:
                    values[value_type] = self._get_last_reported_date()
            except Exception as e:
                log.error(e)

        return values

    def __init__(self):
        self.initialise_url('https://api.abuseipdb.com/api/v2/check')
        self.initialise_api_key("abuseipdb")
        self.failed_request = False
        
        self.website_url = ""
        self.data = {}
        self.reports = []

    def check_ip(self, ip, days=30):
        self.failed_request = False
        headers = super().headers
        headers.accept_json()
        headers.set_custom('Key', self.API_KEY)

        http = super().http

        params = {'ipAddress': ip, 'maxAgeInDays': days, 'verbose':''}
        for key, value in params.items():
            http.param(key, value)
        response = requests.request(method=HTTP.method_get(), url=self.URL, headers=headers.headers, params=http.params)
        if response.status_code == 200:
            json_obj = response.json()
            self.data = json_obj['data']
            self.website_url = f'www.abuseipdb.com/check/{ip}'
            for report in self.data['reports']:
                self.reports.append(
                    Report(date=report['reportedAt'], comment=report['comment'], categories_ids=report['categories']))
        elif response.status_code == 429:
            self._daily_limit_reached = True
        else:
            response_text = response.text if response.text else ""
            log.error("Request failed with status code " + str(response.status_code) + " " + response_text)

        if response.status_code != 200:
            self.failed_request = True
        return self

    def _get_ipaddress(self):
        return self.data['ipAddress']
    
    def _get_public_ip(self):
        return self.data['isPublic']
    
    def _get_abuse_score(self):
        return self.data['abuseConfidenceScore']
    
    def _get_country(self):
        return self.data['countryCode']
    
    def _get_country_name(self):
        return self.data['countryName']
    
    def _get_usage_type(self):
        return self.data['usageType']
    
    def _get_isp(self):
        return self.data['isp']
    
    def _get_domain(self):
        return self.data['domain']
    
    def _get_total_reports(self):
        return self.data['totalReports']
    
    def _get_last_reported_date(self):
        return self.data['lastReportedAt']

    def _get_reports(self):
        return self.reports

    def max_days(self):
        return self._max_days

    def min_days(self):
        return self._min_days

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
        log.info("Parsing AbuseIPDB report categories")
        result_categories = []
        for category_id in categories:
            result_categories.append(Report._report_categories[str(category_id)])

        return result_categories



