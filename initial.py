import mysql.connector as sqlc
import time

user =  input("Enter user : ")
p_word =  input("Type password to database : ")
host = "localhost" #input("Enter host : ")
db_name = input("Enter name of database (shouldn't pre-exits) : ")

mydb = sqlc.connect(user= user, password= p_word,
                              host = host)
my_curser = mydb.cursor()
my_curser.execute("create database " +db_name)
my_curser.execute("use "+db_name)
my_curser.execute("create table cust_details(cust_id varchar(8) not null primary key , name varchar(50), mobile varchar(15) , email varchar(30) , address varchar(100) )")
my_curser.execute("create table order_details(order_id varchar(25) , cust_id varchar(8) , pack_name varchar(30) , from_address varchar(100) , to_address varchar(100))")
mydb.commit()
print("database name :- " +db_name)
print("NOTE :- USE THIS DATABASE NAME IN MAIN PROGRAMME ! ")
time.sleep(4)
E = input("Press ENTER to END ! ")
