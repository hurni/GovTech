# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:38:32 2023

@author: haema
"""


import requests as r
import urllib3



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

s = r.Session()

proxies = None
private_api_key = '0887bd41-1637-4334-a0ad-633b0f557667'
base_url = 'https://ckan.ogdch-abnahme.clients.liip.ch/api/3/action/package_patch'

header = {'Authorization': private_api_key}



# list of adapted ids = 
# add gemeindenames as dct:spatial.  

data = {
        'id': "6fbab091-823e-43df-8b1d-de2c3e6763c9",
        'spatial' : 'Zollikofen'
        }


x = s.post(base_url,data=data,proxies=proxies,headers=header,verify=False)

print(x.status_code)


"""

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


"""


