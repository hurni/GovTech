"""harvester using fetch_urls.sh
"""

import glob
import os
import harvester
import json

output_dir = './output'
extension = 'csv'

def get_data(jsonfile):
    """Read the urls from json file and return the json object"""
    f = open(jsonfile)
    data = json.load(f)
    f.close()
    return data

# It's always nice to create missing directories automatically
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate over all json files in the current directory (output from fetch_urls.sh)
for file in glob.glob("*.json"):
    data = get_data(file)

    # get the domain from the filename
    domain = file.split('.')[0]

    # Create domain subdirectory if necessary
    if not os.path.exists(f"{output_dir}/{domain}"):
        os.makedirs(f"{output_dir}/{domain}")

    mapfile = open(f'{output_dir}/{domain}/mapping.csv', 'w')
    mapfile.write('package_id,ressource_id,filename\n')
    
    # Download each url into a file named xxxxxxxx.csv
    #for i in range(len(data)):
    for i in range(200):
        url = data[i]["url"]
        package_id = data[i]["package_id"]
        ressource_id = data[i]["resource"]
        if 'zip' in url.lower():
            # exclude zip files based on the name
            print(f'{url},ZIP')
            continue
        
        filename = f'{str(i).zfill(8)}.csv'
        try:
            harvester.download_file(url, f'{output_dir}/{domain}/{filename}')
            buf = f'{package_id},{ressource_id},{filename}'
            print(buf)
            mapfile.write(buf+'\n')
        except:
            print(f'{urls[i]},ERROR')

    mapfile.close()
