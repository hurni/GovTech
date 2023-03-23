#!/usr/bin/env bash

curl "https://ckan.opendata.swiss/api/3/action/package_search?fq=groups:territory&rows=1000" | jq '[.result.results[] | .resources[] | select(.format == "CSV") | .download_url]' > territory.json

curl "https://ckan.opendata.swiss/api/3/action/package_search?fq=groups:geography&rows=1000" | jq '[.result.results[] | .resources[] | select(.format == "CSV") | .download_url]' > geography.json
