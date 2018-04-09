import pymongo
import csv
import os

print("Import Initialised")

mc = pymongo.MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],
                         27017)
print("Mongo Client Initialised")

db = mc.nd
print("Database Initialised")

p = os.path.join('..', 'python', 'nesGamesfinal.tsv')

with open(p) as fd:
    rd = csv.reader(fd, delimiter="\t")
    for row in rd:
        try:
            players = int(row[2])
        except ValueError:
            players = 1
        try:
            date = int(row[3])
        except ValueError:
            date = 1989
        try:
            rating = float(row[5])
        except ValueError:
            rating = 5
        try:
            salesNa = float(row[7])
        except ValueError:
            salesNa = row[7]
        try:
            salesEu = float(row[8])
        except ValueError:
            salesEu = row[8]
        try:
            salesJpn = float(row[9])
        except ValueError:
            salesJpn = row[9]
        try:
            salesOther = float(row[10])
        except ValueError:
            salesOther = row[10]
        try:
            salesGlobal = float(row[11])
        except ValueError:
            salesGlobal = row[11]

        a = {'id': row[0],
             'name': row[1],
             'players': players,
             'date': date,
             'publisher': row[4],
             'rating': rating,
             'genre': row[6],
             'salesNa': salesNa,
             'salesEu': salesEu,
             'salesJpn': salesJpn,
             'salesOther': salesOther,
             'salesGlobal': salesGlobal,
             'filename': row[12]
             }
        db.games.insert(a)
