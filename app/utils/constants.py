import os

solr_host = os.getenv("SOLR_HOST", "host.docker.internal")
title_weight_multiplier = os.getenv("ROWS", 20)
text_weight_multiplier = os.getenv("ROWS", 2)
rows = os.getenv("ROWS", 200)

params = f"?fl=score&fl=*&defType=edismax&qf=_title_^{title_weight_multiplier}+_text_^{text_weight_multiplier}&rows={rows}"

headers = {
    'Content-Type': 'application/json'
}

request_object = {
    "query": "query_replacement",
    "facet": {
        "url": {
            "type": "terms",
            "field": "base_url",
            "limit": 10
        },
        "size": {
            "type": "terms",
            "field": "size",
            "limit": 3000
        }
    }
}
