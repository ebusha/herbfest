import sqlite3
from flask import Flask, render_template

app = Flask(__name__)
conn = sqlite3.connect("duke/duke.db")
db = conn.cursor()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/family/")
def get_families(title="Family", f="", genera=[], g="", species=[]):
    return render_template("taxons.html",
                           title=title,
                           families=db.execute('''
                           SELECT family, COUNT(family)
                           FROM fgs GROUP BY family
                           ''').fetchall(),
                           f=f,
                           genera=genera,
                           g=g,
                           species=species)


@app.route("/family/<family>/")
def get_family_genera(family, title="Genus", g="", species=[]):
    return get_families(title=title,
                        f=family,
                        genera=db.execute('''
                        SELECT genus, COUNT(genus)
                        FROM fgs
                        WHERE family=="%s"
                        GROUP BY genus
                        ''' % family).fetchall(),
                        g=g,
                        species=species)


@app.route("/family/<family>/<genus>/")
def get_family_genera_species(family, genus):
    return get_family_genera(family,
                             title="Species",
                             g=genus,
                             species=db.execute('''
                             SELECT species
                             FROM fgs
                             WHERE family=="%s" and genus=="%s"
                             ''' % (family, genus)).fetchall())
