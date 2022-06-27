from bs4 import BeautifulSoup
import requests
import re

from email_validator import validate_email, EmailNotValidError, caching_resolver
from email_validator import validate_email, caching_resolver
resolver = caching_resolver(timeout=10)
from validate_email import validate_email

from email_validate import validate, validate_or_fail

import whois


email = "info1111@ryansplus.com"

# domains = email[email.index('@') + 1 : ]
# print('domains', domains)

# details = whois.whois(domains)
# print('details',details)
# server=details.name_servers
# smtp =(domains.replace('.com', ''))
# dns=details.dnssec
# print('server',server)
# print('dns',dns)
# print('smtp',smtp)

# temp = re.compile("([a-zA-Z]+)([0-9]+)")
res = [re.findall(r'(\w+?)', email)[0] ]
print('res', res)

