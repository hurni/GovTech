"""harvester using fetch_urls.sh
"""

import glob
import os
import harvester
import json

output_dir = './output'
extension = 'csv'

def get_urls(jsonfile):
    f = open(jsonfile)
    data = json.load(f)
    f.close()
    return data

# It's always nice to create missing directories automatically
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for file in glob.glob("*.json"):
    urls = get_urls(file)
    # get the domain from the filename
    domain = file.split('.')[0]

    # Create domain subdirectory if necessary
    if not os.path.exists(f"{output_dir}/{domain}"):
        os.makedirs(f"{output_dir}/{domain}")

    for i in range(len(urls)):
        filename = f'{output_dir}/{domain}/{str(i).zfill(8)}'
        harvester.download_file(urls[i], filename)
        print(f'{urls[i]},{filename}.{extension}')


