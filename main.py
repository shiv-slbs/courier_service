import mysql.connector as sqlc
import sys
import keyboard
import time

p_word = "shiv703338"# input ("Type password to database : ")
mydb = sqlc.connect(user='root', password= p_word,
                              host='localhost',
                              database='slbs_service')
my_curser = mydb.cursor()

def main ():
    print ('''
    Main Menu
    *********
    1.Show customer detials
        a.all customer details
        b.individual customer detials

    2.Show order details
        a.all order details
        b.specific order detials
        
    3.Add new customer profile
    4.Add new order
    5.exit
    ''')

    ch = input ("Enter no. according to your execution : ")
    match ch:
        case '1':
            cust_details()
        case '2':
            order_details()
        case '3':
            add_cust()
        case '4':
            add_order()
        case '5':
            exit()
        case other:
            print("MAdarchod bakchodi nhi karo")
            main()

           

def cust_details():
    print ('''
        1.Show all customers detais
        2.Show an individual's details
        3.Main Menu
        ''')
    var_ch1 = input("Enter no. according to your execution : ")
    match var_ch1:
        case "1":
            my_curser.execute('select * from cust_details')
            rec = my_curser.fetchall()
            for i in rec:
                print(i)
                # print("\n")
            time.sleep(1.5)
            E = input("Press Enter to naviagte to MAIN MENU.")
            main()
        case "2":
            c_id = input ("Enter customer ID of the customer : ")
            my_curser.execute("select * from cust_details where cust_id = '" +c_id+ "'")
            rec = my_curser.fetchall()
            print(rec)
            time.sleep(1.5)
            E = input("Press Enter to naviagte to MAIN MENU.")
            main()

        case '3':
            main()
        case other:
            main()

def order_details():
    print ('''
        1.Show all order detais
        2.Show a specific order details
        3.Main Menu
        ''')
    var_ch2 = input("Enter no. according to your execution : ")
    match var_ch2:
        case "1":
            my_curser.execute("select * from order_details")
            rec = my_curser.fetchall()
            for i in rec:
                print(i)
                print("\n")
            time.sleep(1.5)
            E = input("Press Enter to naviagte to MAIN MENU.")
            main()

        case "2":
            o_id = input ("Enter order ID of the order : ")
            my_curser.execute("select * from order_details where order_id = '" +o_id+ "'")
            rec = my_curser.fetchall()
            print(rec)
            time.sleep(1.5)
            E = input("Press Enter to naviagte to MAIN MENU.")
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
    address = input("Enter customer's Address ")

    data_to_add_cust =(c_id , name , Mob , email , address )
    my_curser.execute("INSERT INTO cust_details VALUES (%s, %s, %s, %s,%s)" , data_to_add_cust)
    

    ch_yn = input("Want to add more (Y/N) : ")
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
    from_address = input ("Enter address ''from'' it is sent : ")
    to_address = input("Enter address ''to'' which it is sent : ")

    data_to_add_order =[c_id , o_id , pack_name , from_address , to_address ]
    my_curser.execute("INSERT INTO order_details VALUES (%s, %s)" , data_to_add_order)

    ch_yn = input("Want to add more (Y/N) : ")
    if ch_yn == y or ch_yn == Y :
        add_order()
    elif ch_yn == n or ch_yn == N :
        main()
    else:
        main()

def exit():
    mydb.close()
    sys.exit()

main() 