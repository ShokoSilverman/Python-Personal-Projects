import mysql.connector

mydb = mysql.connector.connect(user='root', password='test',
                              host='127.0.0.1', database="python_db")

print(mydb)

# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE python_db")

#create
# sql = "INSERT INTO test_crud_table (Id, FirstName, LastName, HireYear) VALUES (%s, %s, %s, %s)"
# val = ("0", "Simon", "Silverman", "2003")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")

#read all
# mycursor.execute("SELECT * FROM test_crud_table")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

#read
# sql = "SELECT * FROM test_crud_table WHERE Id = 1"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

#update
# mycursor = mydb.cursor()
# sql = "UPDATE test_crud_table SET FirstName = ' VERA' WHERE Id = 1" #trucated incorrect double value just means you had the wrong value type, not a specific double
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")

#delete
# mycursor = mydb.cursor()
# sql = "DELETE FROM test_crud_table WHERE Id = '0'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")



