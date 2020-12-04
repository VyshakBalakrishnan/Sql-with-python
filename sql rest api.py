import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="12345678",database="testdb")

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE testdb")
mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i)
#inserting data
mycursor.execute("CREATE TABLE products (id INT, name VARCHAR(50), cost INT")
data="INSERT INTO products (id,name,cost) values(%s %s %s)"
products=[(1,"asus",12000),(2,"oppo",11000)]
mycursor.executemany(data,products)
mydb.commit()

#retrieving data
mycursor.execute("SELECT * FROM products")
result=mycursor.fetchall()
for j in result:
    print(j)





