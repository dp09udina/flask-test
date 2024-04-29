cls_query = """
    SELECT ?class WHERE {?class a <http://www.w3.org/2002/07/owl#Class>}
"""

labels_query = """
    prefix owl: <http://www.w3.org/2002/07/owl#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?individual_iri ?individual_label 
    WHERE {?individual_iri a owl:NamedIndividual;
    rdfs:label ?individual_label
    }
"""

subjects_query = """
    SELECT ?subject ?predicate ?object WHERE {?subject ?predicate ?object}
"""
