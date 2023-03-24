#!/usr/bin/env bash

for i in {0..5}; do

    curl "https://ckan.opendata.swiss/api/3/action/package_search?fq=groups:territory&rows=1000&start=$(( $i * 1000))" | jq '[.result.results[] | .resources[] | select(.format == "CSV") | {url: .download_url, resource: .id, package_id: .package_id}]' > territory_$i.json

    curl "https://ckan.opendata.swiss/api/3/action/package_search?fq=groups:geography&rows=1000&start=$(( $i * 1000))" | jq '[.result.results[] | .resources[] | select(.format == "CSV") | {url: .download_url, resource: .id, package_id: .package_id}]' > geography_$i.json

done

jq -s '. | flatten' *.json > sources.json
