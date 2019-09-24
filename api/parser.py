import re
import ipaddress
from api import ioc_type as ioc_type


def remove_domain_prefix(domain):
    """
    Removes the protocl from the start of the domain name (http:// or https://.
    Also removed wwww.
    :param domain: The domain name to trim
    :return: The domain with the protocol and www. removed if they exist.
    """
    if "http" in domain:
        if "https://" in domain:
            domain = domain.replace("https://", "")
        else:
            domain = domain.replace("http://", "")

    if domain[:4] == "www.":
        domain = domain[4:]
    return domain


def remove_port_from_ip(ip):
    return ip.split(":")[0]


def detect_ioc(ioc):
    ioc = ioc.lower()
    if re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}(:[0-9]+)?$", ioc):
        if ipaddress.ip_address(remove_port_from_ip(ioc)).is_private:
            return ioc_type.TYPE_PRIVATE_IP()
        return ioc_type.TYPE_IP()

    if re.match(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", ioc):
        print("VALID")
        return ioc_type.TYPE_EMAIL()
    ioc = remove_domain_prefix(ioc)

    if re.match(r"^[a-f0-9]{32}$", ioc):
        return ioc_type.TYPE_HASH_MD5()
    if re.match(r"[0-9a-f]{40}$", ioc):
        return ioc_type.TYPE_HASH_SHA1()
    if re.match(r"[0-9a-f]{64}$", ioc):
        return ioc_type.TYPE_HASH_SHA256()

    if re.match(r"^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9](?:\.[a-zA-Z]{2,})+$", ioc):
        return ioc_type.TYPE_DOMAIN()
    print("Unable to detect IOC type")

res = detect_ioc("7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069")
print(res)