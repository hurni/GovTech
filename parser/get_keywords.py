import csv
import pandas as pd
import chardet
import os

#get the delimiter of the csv-file
#https://stackoverflow.com/questions/46135839/auto-detect-the-delimiter-in-a-csv-file-using-pd-read-csv
'''
def get_delimiter(file_path, bytes = 4096):
    sniffer = csv.Sniffer()
    data = open(file_path, "r").read(bytes)
    delimiter = sniffer.sniff(data).delimiter
    return delimiter
'''

def get_delimiter(file_path: str) -> str:
    with open(file_path, 'r') as csvfile:
        delimiter = str(csv.Sniffer().sniff(csvfile.read()).delimiter)
        return delimiter
#example

# if not utf-8....
# look at the first ten thousand bytes to guess the character encoding
#https://yunkgao.wordpress.com/2020/09/11/how-to-detect-delimiter-and-encoding-of-csv-file-in-python-pandas/
def get_encoding(filename):
    with open(filename, 'rb') as rawdata:
        result = chardet.detect(rawdata.read(10000))
        encoding = result['encoding']
    return encoding

communityList_path = os.path.join(os.path.dirname(__file__), '..', 'data/EtatCommunes_2023_kurz_comma.csv')
communityList = pd.read_csv(communityList_path)['GemeindeName'].to_list()

def getCommunityNames(fileName):
    namesPresent = ''
    
    df = pd.read_csv(fileName, sep = get_delimiter(fileName), on_bad_lines='skip')
    print(fileName)
    for community in communityList:
        for col in df.columns:
            if (df[col].eq(community)).any():
                namesPresent = namesPresent + community + ', '
                break
    if namesPresent!='':
        namesPresent=namesPresent[:-2]
    return namesPresent

data_path = os.path.join(os.path.dirname(__file__), '..', 'harvester','output/sources/')
df = pd.read_csv(os.path.join(data_path, 'mapping.csv')).iloc[:100]
datafiles_path = os.path.join(os.path.dirname(__file__), '..', 'harvester','output/sources/')
df['filename'] = datafiles_path + df['filename']
df['communities_names'] = df.apply(lambda row: getCommunityNames(row['filename']), axis=1)
df.drop(['ressource_id', 'filename'], axis=1, inplace=True)


export_path = os.path.join(os.path.dirname(__file__), '..', 'export')
df.to_csv(os.path.join(export_path,'test_final.csv'), index=False)
