# -*- coding: utf-8 -*-

import requests as r
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

s = r.Session()
proxies = None
private_api_key = # your API Key from useraccount on backend
patch_url = 'https://ckan.ogdch-abnahme.clients.liip.ch/api/3/action/package_patch'

header = {'Authorization': private_api_key}

# add gemeindenames as dct:spatial.  
"""
list of package_ids
for id in package_ids:
    add d.key(value)


"""

data = {
        'id': "6fbab091-823e-43df-8b1d-de2c3e6763c9", # Example. For automatisation: add list above
        'spatial' : 'Zollikofen'
        }


x = s.post(patch_url,data=data,proxies=proxies,headers=header,verify=False)

# print(x.status_code)
