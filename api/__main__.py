import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.talos import Talos as talos
from api.osint import Osint

test = talos()

print("   VirusTotal Report Link: " + "https://www.virustotal.com/gui/ip-address/" + str("8.8.8.8"))
input()