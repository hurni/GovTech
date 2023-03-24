# Fulltext indexer POC

## Requirements

* (meilisearch)[https://www.meilisearch.com/]


## Usage

If you haven't already built the index, you must build it.
An index is included in GitHub, you can skip point 0 and 2 and just launch meilisearch.

0. Download the jsons and augment them:
```
$ cd harvester
$ python harvester.py 
```

1. Lauch meilisearch
```
$ meilisearch
```

2. Feed the jsons to the index:
```
$ cd ../fulltextindexer
$ ./feedindexer.sh
```

 Go to http://localhost:7700
