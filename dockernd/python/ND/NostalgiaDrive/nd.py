import nd.ndGui
import nd.ndMongo
from os import path, system


# Grab mongodb and output parameters to text
mDb = nd.ndMongo.NdMongo()

# Build Gui to make selections then output to log
y = nd.ndGui.NdGui()

# Grab selections from log and query db
logPath = path.join('..', 'python', 'ND', 'NostalgiaDrive', 'docs', 'log.txt')
selection = mDb.queryGames(logPath)
print(repr(selection))

histPath = path.join('..', 'python', 'ND', 'NostalgiaDrive', 'docs', 'selections','hist.txt')
f= open(histPath,"a+")
f.write(selection)


gamePath = path.join('..', 'python', 'ND', 'data', 'Nintendo', selection).rstrip()

# Add selection to history
hist = path.join('..', 'python', 'ND', 'NostalgiaDrive', 'docs', 'history.txt')
with open(logPath, "r") as f1:
    t1 = f1.readlines()
with open(hist, "r") as f2:
    t2 = f2.readlines()
t2.insert(20, t1)
with open(hist, "w") as f2:
    f2.writelines(t2)

# Run script
sPath = path.join('..', 'python', 'ND', 'NostalgiaDrive', 'docs', 'scripts', 'basic.sh')
system("fceux " + "\"" + gamePath + "\"")

# Close connection to database
mDb.client.close()
