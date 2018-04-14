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
gamePath = path.join('..', 'python', 'ND', 'data', 'Nintendo', selection).rstrip()

# Run script
sPath = path.join('..', 'python', 'ND', 'NostalgiaDrive', 'docs', 'scripts', 'basic.sh')
system("fceux " + "\"" + gamePath + "\"")

# Close connection to database
mDb.client.close()
