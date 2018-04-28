import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='chrx',
                             db='nd',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM games WHERE RATING LIKE '%s'" % ("9%")
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
