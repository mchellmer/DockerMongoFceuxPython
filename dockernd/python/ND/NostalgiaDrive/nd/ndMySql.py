import pymysql.cursors
from os import path, environ

class NdMySql():
    def __init__(self):
        # Connect to the database
        print("MySql Constructed")
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='chrx',
                             db='nd',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        self.outSelections()

    def outSelections(self):
        print("Retrieving Games")
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                sels = ["`genre`","`date`","`players`","`publisher`","`filename`"]
                files = ["genres.txt","dates.txt","players.txt","publishers.txt","all.txt"]
                i=0
                for sel in sels:
                    sql = "SELECT DISTINCT %s FROM games WHERE %s <> ''" % (sel,sel)
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    self.outText(sel,result,files[i])
                    i+=1
        finally:
            self.connection.close()

    def outText(self, selection, results, filename):
        print("Outputing selection file " + filename)
        filepath = path.join('..', 'python', 'ND', 'NostalgiaDrive', 'docs', 'selections', filename)
        filepath = path.join('..','docs', 'selections', filename)
        file = open(filepath, 'w')
        key = selection.replace("`","")
        for result in results:
            file.write(result[key]+'\n')

    def queryGames(self, logPath):
        print("Querying Database")
        file = open(logPath, 'r')
        lines = file.readlines()
        lines.remove('\n')

        if len(lines) > 3:
            query = self.queryLog(lines)
            try:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    result = cursor.fetchone()
                    print(result)
            finally:
                connection.close()

            if result.count() == 0:
                return "Lee Trevino's Fighting Golf.zip"
            else:
                return(result)
        # TODO: What?
        else:
            return(lines[1].rstrip())

    def queryLog(self, lines):
        sql = "SELECT `filename` FROM games WHERE `name` <> 'ET'"
        whereText = ""

        for line in lines:
            line = line.split()
            if line[0] == 'rating':
                if line[1] == 'Min':
                    whereText = " AND CAST(`rating` AS DECIMAL(8,2)) > " + line[2]
                    sql += whereText
                else:
                    whereText = " AND CAST(`rating` AS DECIMAL(8,2)) < " + line[2]
                    sql += whereText
            elif len(line) == 3:
                if line[2] != 'False':
                    whereText = [line[0]]
        print(sql)

a = NdMySql()
a.queryGames(path.join('..','docs', 'log.txt'))
