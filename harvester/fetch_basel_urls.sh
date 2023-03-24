#!/usr/bin/env bash


curl "https://ckan.opendata.swiss/api/3/action/package_search?fq=organization:kanton-basel-stadt&rows=1000" | jq '[.result.results[] | .resources[] | select(.format == "CSV") | {url: .download_url, resource: .id, package_id: .package_id}]' > basel.json


jq -s '. | flatten' *.json > sources.json
