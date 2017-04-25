from collections import Counter
import sqlite3

conn = sqlite3.connect("duke/duke.db")
db = conn.cursor()


def format(bind, data, title):
    return {'bindto': bind,
            'data': {'columns': [[k, v] for k, v in data.items()],
                     'type': 'donut'},
            'donut': {'title': title}}


def get_activities(chem):
    return [act[0] for act in db.execute('''
    SELECT activity
    FROM aggregac
    WHERE chem=="%s"
    ''' % chem).fetchall()]


def get_super_activities(act):
    return [sact[0] for sact in db.execute('''
    SELECT superact
    FROM superact
    WHERE activity=="%s"
    ''' % act).fetchall()]


def make_summary(f, g, s):
    fnfnum, taxon = db.execute('''
    SELECT fnfnum, taxon
    FROM fnftax
    WHERE family=="%s" AND genus=="%s" AND species=="%s"
    ''' % (f, g, s)).fetchall()[0]

    
    cnames = [name[0] for name in
              db.execute('''
              SELECT cnnam
              FROM common_names
              WHERE fnfnum=="%s"
              ''' % fnfnum).fetchall()]

    # Don't forget to grab dosages later.
    # The dosages in aggregac and dosages are different.
    chems_classes = db.execute('''
    SELECT chem, chemclass
    FROM farmacy_new
    WHERE fnfnum=="%s"
    ''' % fnfnum).fetchall()
    chems = [chem[0] for chem in chems_classes]

    acts = []
    for c in chems:
        acts.extend(get_activities(c))
    acts_sum = {a: acts.count(a) for a in set(acts)}
    acts_sum = dict(Counter(acts_sum).most_common(10))

    super_acts = []
    for a in acts:
        super_acts.extend(get_super_activities(a))
    super_acts_sum = {sa: super_acts.count(sa) for sa in set(super_acts)}
    super_acts_sum = dict(Counter(super_acts_sum).most_common(10))

    return {"taxon": taxon,
            "cnames": cnames,
            # The one with classes was used since the other is only
            # used as an aggregate.
            "chems": chems_classes,
            "acts": acts_sum,
            "sup_acts": super_acts_sum}


def get_summary(f, g, s):
    temp = make_summary(f, g, s)
    temp['acts'] = format("#activities-chart",
                          temp['acts'],
                          "Chemical Activities")
    temp['sup_acts'] = format("#superactivities-chart",
                              temp['sup_acts'],
                              "Chemical Syndromes")
    return temp
