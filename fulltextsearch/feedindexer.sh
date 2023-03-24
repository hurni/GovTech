#!/bin/bash

cd ../harvester/output
for file in *.json; do
	echo $file
	curl -X POST 'http://127.0.0.1:7700/indexes/main/documents?primaryKey=meilisearch_id' -H 'Content-Type: application/json' --data-binary @$file
done

