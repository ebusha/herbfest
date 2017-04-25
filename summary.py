import sqlite3

conn = sqlite3.connect("duke/duke.db")
db = conn.cursor()

f = "Brassicaceae"
g = "Lepidium"
s = "meyenii"
fnfnum = "2388"
q = (f, g, s)
chem = "ZINC"
act = 'Antitumor'


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


def fgs_get_summary(f, g, s):
    fnfnum = db.execute('''
    SELECT fnfnum
    FROM fnftax
    WHERE family=="%s" AND genus=="%s" AND species=="%s"
    ''' % (f, g, s)).fetchall()[0][0]

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

    super_acts = []
    for a in acts:
        super_acts.extend(get_super_activities(a))
    super_acts_sum = {sa: super_acts.count(sa) for sa in set(super_acts)}

    return {"cnames": cnames,
            # The one with classes was used since the other is only
            # used as an aggregate.
            "chems": chems_classes,
            "acts": acts_sum,
            "sup_acts": super_acts_sum}
