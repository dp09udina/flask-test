from flask import Blueprint, render_template
from tools.const import cls_query, labels_query, subjects_query
from tools.func import query

""" blueprint """
views = Blueprint(__name__, "views")


@views.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@views.route("/classes")
def classes():
    results = query(cls_query)

    return render_template("classes.html", result=results["results"]["bindings"])


@views.route("/subjects")
def subjects():
    results = query(subjects_query)

    return render_template("subjects.html", result=results["results"]["bindings"])


@views.route("/labels")
def labels():
    results = query(labels_query)

    return render_template("labels.html", result=results["results"]["bindings"])
