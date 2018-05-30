import pymysql
from pymysql import MySQLError

# Connect to the database
connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='guest_book',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Do the CRUD here:
		# e.g. Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # connection.commit()
except MySQLError as e:
    print("Failed to connect to the database: " + e)
finally:
    connection.close()