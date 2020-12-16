from tinydb import TinyDB, Query

db = TinyDB('./db/db.json')

table = db.table('fichas')
table.insert({'value': True})
print(table.all())