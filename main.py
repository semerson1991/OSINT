import osint.api.utils as utils
import osint.api.comms as comms

from osint.api.virus_total import VirusTotal
from osint.api.abuseipdb import AbuseIPDB

abuse = AbuseIPDB()
abuse.check_ip("8.8.8.8")
#print("{vt.API_KEY}".format(vt=VirusTotal()))
# virus_total.check_ip("43.43.43.55")
# input()
