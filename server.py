import sqlite3
from flask import Flask, render_template

app = Flask(__name__)
conn = sqlite3.connect("duke/duke.db")
db = conn.cursor()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/family/")
def get_families():
    return render_template("family.html",
                           title="Family",
                           results=db.execute('''
                           SELECT family, COUNT(family)
                           FROM fgs GROUP BY family
                           ''').fetchall())


@app.route("/family/<family>/")
def get_family_genus(family):
    return render_template("genus.html",
                           title="Genus",
                           f=family,
                           families=db.execute('''
                           SELECT family, COUNT(family)
                           FROM fgs GROUP BY family
                           ''').fetchall(),
                           genera=db.execute('''
                           SELECT genus, COUNT(genus)
                           FROM fgs
                           WHERE family=="%s"
                           GROUP BY genus
                           ''' % family).fetchall())


@app.route("/family/<family>/<genus>/")
def get_family_genus_species(family, genus):
    return render_template("species.html",
                           title="Genus",
                           f=family,
                           families=db.execute('''
                           SELECT family, COUNT(family)
                           FROM fgs GROUP BY family
                           ''').fetchall(),
                           g=genus,
                           genera=db.execute('''
                           SELECT genus, COUNT(genus)
                           FROM fgs
                           WHERE family=="%s"
                           GROUP BY genus
                           ''' % family).fetchall(),
                           species=db.execute('''
                           SELECT species
                           FROM fgs
                           WHERE family=="%s" and genus=="%s"
                           ''' % (family, genus)).fetchall())
