import csv
import pandas as pd

#get the delimiter of the csv-file
#https://stackoverflow.com/questions/46135839/auto-detect-the-delimiter-in-a-csv-file-using-pd-read-csv

def get_delimiter(file_path, bytes = 4096):
    sniffer = csv.Sniffer()
    data = open(file_path, "r").read(bytes)
    delimiter = sniffer.sniff(data).delimiter
    return delimiter

#example

df = pd.read_csv(exampleFile, sep = get_delimiter(exampleFile))