from fastapi import APIRouter
from utils.constants import solr_host, request_object, params, headers
from utils.query_cleaner import query_cleaner
import json
import traceback
import requests

router = APIRouter()


@router.get("/query")
async def query_endpoint(query: str):
    try:
        first_response = requests.post(f"http://{solr_host}:8983/solr/mycore/query{params}", headers=headers,
                                       data=json.dumps(request_object).replace("query_replacement", query).encode('utf-8'))
        first_response_json = first_response.json()
        if first_response_json['response']['numFound'] > 0:
            return {"results": [first_response_json]}

        query_cleaner_object = query_cleaner()

        fuzzy_query = query_cleaner_object.get_clean_query(query)
        second_response = requests.post(f"http://{solr_host}:8983/solr/mycore/query{params}", headers=headers, data=json.dumps(
            request_object).replace("query_replacement", fuzzy_query).encode('utf-8'))
        second_response_json = second_response.json()
        return {"results": [second_response_json]}

    except BaseException as ex:
        return {"results": [traceback.format_exc()]}


@router.get("/suggest")
async def suggest_endpoint(q: str):
    try:
        suggest_response = requests.get(
            f"http://{solr_host}:8983/solr/mycore/suggest?suggest=true&suggest.build=true&suggest.dictionary=mySuggester&wt=json&suggest.q={q}".encode('utf-8'))
        suggest_json = suggest_response.json()
        return {"results": suggest_json}
    except BaseException as ex:
        return []
