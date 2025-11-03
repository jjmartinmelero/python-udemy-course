import mysql.connector

people_db = mysql.connector.connect(
    host="sql7.freesqldatabase.com",
    user="sql7805841",
    password="CInU3u9Cwv",
    database="sql7805841"
)

# select

cursor = people_db.cursor()
cursor.execute('SELECT * FROM people')
result = cursor.fetchall()

for person in result:
    print(person)

# insert
# setence = 'INSERT INTO people(name, last_name, age) VALUES(%s, %s, %s)'
# values = ('Juan Jesus', 'Last Name', 31)
# cursor.execute(setence, values)
# people_db.commit()

# update
# setence = 'UPDATE people SET name=%s, last_name=%s, age=%s WHERE id=%s'
# values = ('Test name', 'test Last Name', 1, 1)
# cursor.execute(setence, values)
# people_db.commit()

# delete
# sentence = 'DELETE FROM people where id=%s'
# values = (1,)
# cursor.execute(sentence, values)
# people_db.commit()

cursor.close()
people_db.close()

