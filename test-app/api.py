from config.config import Config
from flask import Blueprint, render_template, request
from SPARQLWrapper import JSON, SPARQLWrapper
from tools.func import query

""" blueprint """
api_v0 = Blueprint(__name__, "api_v0")


@api_v0.route("/api/v0", methods=["POST"])
def api():
    content_type = request.headers.get("Content-Type")
    data = request.json
    assert content_type == "application/json"

    response = query(data["query"])
    if response["results"]["bindings"]:
        return [i for i in response["results"]["bindings"]]
    else:
        return response
