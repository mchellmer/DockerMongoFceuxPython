import pymongo
import csv

print("Import Initialised")

mc = pymongo.MongoClient()
print("Mongo Client Initialised")

db = mc.nd
print("Database Initialised")

with open("nesGamesfinal.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t")
    for row in rd:
        a = {'id': row[0],
             'name': row[1],
             'players': row[2],
             'date': row[3],
             'publisher': row[4],
             'rating': row[5],
             'genre': row[6],
             'salesNa': row[7],
             'salesEu': row[8],
             'salesJpn': row[9],
             'salesOther': row[10],
             'salesGlobal': row[11],
             'filename': row[12]
             }
        db.games1.insert(a)

print("Entries Added")
print(db.games1.find())
