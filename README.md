# GovTech: 

# opendata.swiss: Automatisiertes Anreichern von Metadaten

## challenge
find the challenge here: https://hack.opendata.ch/project/947

## Goal
Die Metadaten auf opendata.swiss sollen automatisiert angereichert werden, damit geographische Untereinheiten (z.B. Gemeinden, Kantone) bei der Suche 
nach Datasets gefunden werden, obschon sie nicht in den Metadaten aufgeführt sind.
Gewählter Ansatz: Parse the datasets and add tag, if a Gemeinde is mentioned.

## scope
- limit to csv-files on opendata.swiss.
- limit to downloadfiles < 5 MB

## todo

- get the download links from opendata.swiss
- harvest files from download links
- create list of all Gemeinden
- parse the files to find all Gemeinden (i.e. "Zollikofen")
- documentation


## resources

- https://www.opendata.swiss
- Informationen zur Nutzung der API finden sich im Handbook (https://handbook.opendata.swiss/de/content/nutzen/api-nutzen.html) sowie auf der offiziellen Dokumentation von CKAN (https://docs.ckan.org/en/2.9/api/#making-an-api-request)
- Metadaten-Standard DCAT AP-CH (https://dcat-ap.ch/) und die Implementation auf opendata.swiss (https://handbook.opendata.swiss/de/content/glossar/bibliothek/dcat-ap-ch.html)
- github repository of handbook: https://github.com/opendata-swiss/

## To do (future):
implement on productive environment
add kantons
add for geodata. -> cp. https://davidoesch.github.io/geoservice_harvester_poc/

