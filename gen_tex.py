# gen_tex.py
"""
Generate authorlist .tex files
"""

import yaml

db_dir = "yml_dbs/"
db_fn = ["cyber-i.yml", "graduate.yml", "postdoc.yml", "senior.yml"]

members = [] # empty list of members

# add all members to list
for db in db_fn:
    db = db_dir + db
    with open(db, "r") as f:
        yml = yaml.load(f)
        for entry in yml:
            try:
                given_name, surname = entry['name'].split()
                members.append({'aff':entry['affiliation'],
                                'loc':entry['location'],
                                'status':entry['status'],
                                'gname':given_name,
                                'sname':surname})
            except:
                print(entry['name'])

# alphabetically sort members and extract subsets
alphed = sorted(members, key=lambda k: k['sname'])
mem_full = [x for x in alphed if x['status']=='full']

# print to file!
author_entry = "\\author{{{gname} {sname}}}\n\\affiliation{{{aff}, {loc}}}\n"
with open('full_members_test.tex', "w") as f:
    for member in mem_full:
        print(author_entry.format(**member), file=f)
