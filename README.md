# GovTech: 

# opendata.swiss: Automatisiertes Anreichern von Metadaten

## Kontext
Projekt entstand am govtech-hackathon 2023. Die Challenge ist hier zu finden: https://hack.opendata.ch/project/947

## Ziel
Die Metadaten auf opendata.swiss sollen automatisiert angereichert werden, damit geographische Untereinheiten (z.B. Gemeinden, Kantone) bei der Suche 
nach Datasets gefunden werden, obschon sie nicht in den Metadaten von https://www.opendata.swiss aufgeführt sind.
Gewählter Ansatz: Brute Force. Parse the datasets and add tag, if a Gemeinde is mentioned.


## Scope PoC
- Auswahl von 300 Datasets
- Beschränkung auf Datasets mit csv-Ressourcen.
- Beschränkung auf downloadfiles < 5 MB


## todo

- Liste der download-Links mit den entsprechenden Package- und Ressourcen-IDs. > ./harvester
- Harvesten der Datasets > onedrive.com/...
- Liste aller Gemeindenamen > ./data
- Parsen der Downloadfile nach den Gemeindenamen > ./parser
- POST der gefundenen Gemeindanamen auf das entsprechende Dataset
- Dokumentieren!


## zusätzliche Infos: 

- https://www.opendata.swiss
- Informationen zur Nutzung der API finden sich im Handbook (https://handbook.opendata.swiss/de/content/nutzen/api-nutzen.html) sowie auf der offiziellen Dokumentation von CKAN (https://docs.ckan.org/en/2.9/api/#making-an-api-request)
- Metadaten-Standard DCAT AP-CH (https://dcat-ap.ch/) und die Implementation auf opendata.swiss (https://handbook.opendata.swiss/de/content/glossar/bibliothek/dcat-ap-ch.html)
- github repository des opendata.swiss-handbook: https://github.com/opendata-swiss/

## To do (future):

- Ausweiten auf weitere Parameter
- Für die Einbindung von Geodaten. -> cp. https://davidoesch.github.io/geoservice_harvester_poc/
- Produktivsetzung: 
  - Automatisierung nach dem Harvesting (vorausgesetzt: Einwilligung der Datapublisher)
  - Service für Datapublisher, damti sie selber die Metadaten ergänzen.  
