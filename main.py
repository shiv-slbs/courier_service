import mysql.connector as sqlc
import sys
import time

user =  input("Enter user : ")
p_word = input("Type password to database : ")
host = "localhost" #input("Enter host : ")
database = input("Enter database : ")
cust_details = "cust_details" #input("Enter name of Table containing details of customer : ")
order_details = "order_details" #input("Enter name of Table containing details of order : ")

mydb = sqlc.connect(user= user, password= p_word,
                              host = host ,
                              database= database)
my_curser = mydb.cursor()

def main ():
    print ('''
    Main Menu
    *********
    1.Show customer detials
        1.All customer details
        2.Individual customer detials

    2.Show order details
        1.All order details
        2.Specific order detials
        
    3.Add new customer profile
    4.Add new order

    5.Delet customer detail
    6.Delet order details
    
    7.exit
    ''')
    ch = input ("Enter no. according to your execution : ")
    match ch:
        case '1':
            cust_details_()
        case '2':
            order_details_()
        case '3':
            add_cust()
        case '4':
            add_order()
        case '5':
            del_cust_detail()
        case '6':
            del_order_detail()
        case '7':
            exit()
        case other:
            print("Use the programme wisely, dont't be stupid..!")
            main()
          
def cust_details_():
    print ('''
        1.Show all customers detais
        2.Show an individual's details
        3.Main Menu
        ''')
    var_ch1 = input("Enter no. according to your execution : ")
    match var_ch1:
        case "1":
            my_curser.execute("select * from " +cust_details)
            rec = my_curser.fetchall()
            for i in rec:
                print(i)
                # print("\n")
            time.sleep(1.5)
            print("\n")
            E = input("Press Enter to naviagte to MAIN MENU.")
            print("\n")
            main()

        case "2":
            c_id = input ("Enter customer ID of the customer : ")
            my_curser.execute("select * from " + cust_details +" where cust_id = '" +c_id+ "'")
            rec = my_curser.fetchall()
            print(rec)
            time.sleep(1.5)
            print("\n")
            E = input("Press Enter to naviagte to MAIN MENU.")
            main()

        case '3':
            main()
        case other:
            main()

def order_details_():
    print ('''
        1.Show all order detais
        2.Show a specific order details
        3.Main Menu
        ''')
    var_ch2 = input("Enter no. according to your execution : ")
    match var_ch2:
        case "1":
            my_curser.execute("select * from  " + order_details)
            rec = my_curser.fetchall()
            for i in rec:
                print(i)
                # print("\n")
            time.sleep(1.5)
            print("\n"*2)
            E = input("Press Enter to naviagte to MAIN MENU.")
            main()

        case "2":
            o_id = input ("Enter order ID of the order : ")
            my_curser.execute("select * from " +order_details+ " where order_id = '" +o_id+ "'")
            rec = my_curser.fetchall()
            print(rec)
            time.sleep(1.5)
            print("\n"*2)
            E = input("Press Enter to naviagte to MAIN MENU. ")
            main()

        case '3':
            main()
        case other:
            main()

def add_cust():
    c_id = input ("Enter customer ID : ")
    name = input("Enter customer's Name : ")
    Mob = input("Enter customer's Mobile number : ")
    email = input("Enter customer's Email : ")
    address = input("Enter customer's Address : ")

    data_to_add_cust = ( c_id , name , Mob , email, address )
    my_curser.execute("INSERT INTO cust_details VALUES (%s, %s, %s, %s,%s)" , data_to_add_cust)
    mydb.commit()
    time.sleep(1.5)
    print("\n")

    ch_yn = input("Want to add more ?  (Y/N) : ")
    match ch_yn:
        case "y":
            add_cust()
        case "Y":
            add_cust()
        case "N":
            main()
        case "n":
            main()
        case other:
            main()

def add_order():
    c_id = input ("Enter customer ID : ")
    o_id = input ("Enter order ID : ")
    pack_name = input("Enter package name : ")
    from_address = input ("Enter address 'from' it is sent : ")
    to_address = input("Enter address 'to' which it is sent : ")

    data_to_add_order =[c_id , o_id , pack_name , from_address , to_address ]
    my_curser.execute("INSERT INTO order_details VALUES (%s, %s, %s, %s,%s)" , data_to_add_order)
    mydb.commit()
    time.sleep(1.5)
    print("\n")

    ch_yn = input("Want to add more ?  (Y/N) : ")
    match ch_yn:
        case "y":
            add_order()
        case "Y":
            add_order()
        case "N":
            main()
        case "n":
            main()
        case other:
            main()

def del_cust_detail():
    print ('''
        1.Delet a customer's details
        2.Delet all customers details
        3.Main Menu
        ''')
    ch_1 = input("Enter number according to your execution : ")
    match ch_1:
        case '1':
            c_id = input("Enter customer ID of the individual : ")
            my_curser.execute("DELETE FROM "+cust_details+" where cust_id = '" +c_id+ "'")
            mydb.commit()
            time.sleep(1.5)
            print("\n")
            ch_yn = input("Want to delet more ? (Y/N) : ")
            match ch_yn:
                case "y":
                    del_cust_detail()
                case "Y":
                    del_cust_detail()
                case "N":
                    main()
                case "n":
                    main()
                case other:
                    main()
        
        case '2':
            ch_yn = input("Please confirm (Y/N) deletion of all record of customers : ")
            match ch_yn:
                case "y":
                    my_curser.execute("DELETE FROM "+cust_details)
                    mydb.commit()
                    time.sleep(1.5)
                    print("\n")
                    print("All customer deleted.") 
                    print("\n")  
                    E = input("Press Enter to navigate to Main Menu.")
                    main()
                case "Y":
                    my_curser.execute("DELETE FROM "+cust_details)
                    mydb.commit()
                    print("\n")
                    time.sleep(1.5)
                    print("All customer deleted.")
                    print("\n")  
                    E = input("Press Enter to navigate to Main Menu. ")
                    main()
                case "N":
                    main()
                case "n":
                    main()
                case other:
                    main()

def del_order_detail():
    print ('''
        1.Delet a specific order details
        2.Delet all order details
        3.Main Menu
        ''')
    ch_1 = input("Enter number according to your execution : ")
    match ch_1:
        case '1':
            o_id = input("Enter order ID of the individual : ")
            my_curser.execute("DELETE FROM "+order_details+" where order_id = '" +o_id+ "'")
            mydb.commit()
            time.sleep(1.5)
            print("\n")
            ch_yn = input("Want to delet more ? (Y/N) : ")
            match ch_yn:
                case "y":
                    del_order_detail()
                case "Y":
                    del_order_detail()
                case "N":
                    main()
                case "n":
                    main()
                case other:
                    main()

        case '2':
            ch_yn = input("Please confirm (Y/N) deletion of all record of orders : ")
            match ch_yn:
                case "y":
                    my_curser.execute("DELETE FROM "+order_details)
                    mydb.commit()
                    time.sleep(1.5)
                    print("\n")
                    print("All orders deleted.")
                    print("\n") 
                    E = input("Press Enter to navigate to Main Menu. ")
                    main()    
                case "Y":
                    my_curser.execute("DELETE FROM "+order_details)
                    mydb.commit()
                    time.sleep(1.5)
                    print("\n")
                    print("All orders deleted.")
                    print("\n") 
                    E = input("Press Enter to navigate to Main Menu. ")
                    main()
                case "N":
                    main()
                case "n":
                    main()
                case other:
                    main()
        case '3':
            main()
        case other:
            main()

def exit():
    mydb.commit()
    mydb.close()
    print("\n")
    print("************* Programme ENDED..! *************")
    time.sleep(2.5)
    sys.exit()

main()
