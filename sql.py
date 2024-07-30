import mysql.connector as mysql



connection = mysql.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                                       passwd="Logesh@121!",  # your password
                     db="gemini") 
cursor= connection.cursor()


# table_info=""" CREATE table mytable( name varchar(20), age int, phone varchar(10),edu varchar(20) )"""
# cursor.execute(table_info)
cursor.execute(''' INSERT into mytable values('logesh',19,'9940992700','IT') ''')
cursor.execute(''' INSERT into mytable values('loki',20,'99409920','cse') ''')
cursor.execute(''' INSERT into mytable values('mukesh',30,'99409700','eee') ''')
cursor.execute(''' INSERT into mytable values('sakthi',27,'99409900','ece') ''')

print("vaalues are inserted")

cursor.execute('SELECT name from mytable')
data = cursor.fetchall()
for row in data :
    print(row)

connection.commit()
connection.close()