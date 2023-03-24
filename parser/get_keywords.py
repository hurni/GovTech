import csv
import pandas as pd
import chardet

#get the delimiter of the csv-file
#https://stackoverflow.com/questions/46135839/auto-detect-the-delimiter-in-a-csv-file-using-pd-read-csv

def get_delimiter(file_path, bytes = 4096):
    sniffer = csv.Sniffer()
    data = open(file_path, "r").read(bytes)
    delimiter = sniffer.sniff(data).delimiter
    return delimiter

#example

# if not utf-8....
# look at the first ten thousand bytes to guess the character encoding
def get_encoding(filename):
    with open(filename, 'rb') as rawdata:
        result = chardet.detect(rawdata.read(10000))
        encoding = result['encoding']
    return encoding


communityList = pd.read_csv('../data/EtatCommunes_2023_kurz_comma.csv')['GemeindeName'].to_list()

def getCommunityNames(fileName):
    namesPresent = ''
    
    df = pd.read_csv(fileName, sep = get_delimiter(fileName))
    
    for col in df.columns:
        for community in communityList:
            if (df[col].eq(community)).any():
                namesPresent = namesPresent ++ community
    
    return namesPresent

df = pd.read_csv('data/test.csv')
df['communities_names'] = df.apply(lambda row: getCommunityNames(row['fileNames']), axis=1)

df.to_csv('data/test_final.csv', index=False)
