"""Harvester functions to download csv or json resources from opendata.swiss API

NOTE: most of this crap can be avoided if you have bash, curl and fq,
see fetch_urls.sh. The only things you need are the proxy settings as
well as function download_file()

"""

import requests
import urllib3
import os
import socket
import ipaddress
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Add proxy settings for computers on the BV-Netz
hostname = socket.gethostname()

if ipaddress.ip_address(socket.gethostbyname(hostname)) in ipaddress.ip_network('10.194.0.0/16'):
    proxies = {
        "http":'http://proxy-bvcol.admin.ch:8080',
        "https":'http://proxy-bvcol.admin.ch:8080'
    }
else:
    proxies = None
    
s = requests.Session()

# base url for downloading
base_URL = "https://ckan.opendata.swiss/api/3/action/package_show?id="

def get_packages(query):
    return s.get(query,
                 proxies=proxies,
                 verify=False).json()["result"]

def get_resources(package, format = 'CSV'):
    resources = []
    for resource in package["resources"]:
        if resource["format"] == format:
            resources.append(resource)
    return resources

def get_urls(resources):
    urls = []
    for resource in resources:
        urls.append(resource["download_url"])
    return urls

def download_file(url, name = 'test.csv'):
    fcontent = s.get(url,
                     proxies=proxies,
                     verify=False).content
    fout = open(name, 'wb')
    fout.write(fcontent)
    fout.close()

def augment_json(filename, id, url):
    """Add two fields for meilisearch: id and download_url"""
    f = open(jsonfile)
    data = json.load(f)
    f.close()
    data['meilisearch_id'] = id
    data['download_url'] = url
    f = open(jsonfile, 'w')
    f.write(json.dumps(data))
    f.close()

# TODO: really, really rewrite this
def download_files(domain = 'territory',
                   format = 'CSV',
                   output_dir = 'output',
                   max_rows=1000):
    # Create missing directories
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(f"{output_dir}/{domain}"):
        os.makedirs(f"{output_dir}/{domain}")
        
    query = f'https://opendata.swiss/api/3/action/package_search?fq=groups:{domain}&rows={max_rows}'
    urls = []
    for package in get_packages(query)['results']:
        resources = get_resources(package, format)
        urls += get_urls(resources)
        
    for i in range(len(urls)):
        filename = f'{output_dir}/{domain}/{str(i).zfill(8)}'
        if format == 'CSV':
            filename += '.csv'
        elif format == 'JSON':
            filename += '.json'
        else:
            print(f"Unrecognized format: {format}")
            return
        print(f"{urls[i]},{filename}")
        download_file(urls[i], filename)
        if format == 'JSON':
            augment_json(filename, id=i, url=urls[i])
            

        
if __name__ == "__main__":
    format = 'JSON'
    max_rows = 50
    # max_rows limits the number of files retrieved, remove it to
    # download everything
    download_files('territory', format = format, max_rows = max_rows)
    download_files('geography', format = format, max_rows = max_rows)
