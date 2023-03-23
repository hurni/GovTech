# -*- coding: utf-8 -*-

import requests
import urllib3
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {
    "http":'http://proxy-bvcol.admin.ch:8080',
    "https":'http://proxy-bvcol.admin.ch:8080'
}
s = requests.Session()

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

def download_files(domain = 'territory', format = 'CSV', output_dir = 'output', max_rows=1000):
    # It's always nice to create missing directories automatically
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
        print(f"Downloading {urls[i]} to {filename}...")
        download_file(urls[i], filename)

if __name__ == "__main__":
    # max_rows limits the number of files retrieved, remove it to
    # download everything
    download_files('territory', format = 'CSV', max_rows=50)
    download_files('geography', format = 'CSV', max_rows=50)
