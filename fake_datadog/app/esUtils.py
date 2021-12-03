#elastic utilities to insert data into elasticsearch

import os, json, sys
from datetime import datetime
from elasticsearch import Elasticsearch,helpers

ES_HOST = os.getenv("ES_HOST", "http://localhost:9200/")

es = Elasticsearch([ES_HOST], http_compress=True)
es.indices.create(index='test-index', ignore=400)

def bulk_insert_es(index, data):
    bulk_data = ({'_type':'events', '_index':index, **d}
                for d in data)
    helpers.bulk(es,bulk_data)