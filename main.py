from flask import Flask,render_template, request
import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="188.166.221.246",
  user ="training",
  passwd ="training",
  database = "employees"
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()
  
query = "select * from employees order by 1 asc limit 100"
cursorObject.execute(query)
   
myresult = cursorObject.fetchall()
   
for x in myresult:
    print(x)
 
# disconnecting from server
# dataBase.close()

app.run(host='localhost', port=5000)