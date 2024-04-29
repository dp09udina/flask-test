from config.config import Config
from SPARQLWrapper import JSON, SPARQLWrapper

endpoint = Config.CONFIG["database"]["sparql_endpoint"]
sparql = SPARQLWrapper(endpoint)


def query(text_query: str):
    sparql = SPARQLWrapper(endpoint)
    sparql.setTimeout(55)
    sparql.setQuery(text_query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()
