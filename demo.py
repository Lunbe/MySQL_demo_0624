#from flask import ctx
import mysql.connector

print("建立資料庫連線中")
cnx=mysql.connector.connect(

    host="127.0.0.1",
    port=3306,
    user="dbuser",
    password="1234",
    database="world"
)

print("透過連線取得cursor物件")

dbcursor=cnx.cursor()
print("執行select name form city") #否則就要 select * from database.table
print("記得開權限") #就是在MYSQLworkbench中跑程式的內容

dbcursor.execute("select name from world.city")

for cityname in dbcursor:
    print(cityname)

dbcursor.execute("select name, population from world.country")
for(c , p) in dbcursor:
    print(c , p)

