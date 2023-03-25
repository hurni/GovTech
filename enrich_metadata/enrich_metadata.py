
import requests as r
import urllib3
import pandas as pd


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

df = pd.read_csv("https://raw.githubusercontent.com/hurni/GovTech/main/export/test_final.csv")

s = r.Session()

proxies = None

private_api_key = YOUR-PRIVATE-API_KEY # see your Accountinformation on opendata.swiss

patch_url = 'https://ckan.opendata.swiss/api/3/action/package_patch'

header = {'Authorization': private_api_key}

for index, row in df.iterrows():
      
    data = {
            'id': str(row['package_id']),
            'spatial' : str(row['communities_names'])
            }
    
    #print(data)
    
    x = s.post(patch_url,data=data,proxies=proxies,headers=header,verify=False)
    print(x.status_code)
