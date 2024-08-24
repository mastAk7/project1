import mysql.connector as c

def regis():
    cn=c.connect(host='localhost',user='root',passwd='',database='mak')
    cur=cn.cursor()
    print("Please enter the following details for registration")
    print()
    global name,phone,email,passw,addr
    name=input("Name: ")
    phone=int(input("Phone number: "))
    email=input("Email ID: ")
    addr=''
    print()
    passw=input("Please setup a password: ")
    print()
    s="insert into regis values('{}',{},'{}','{}','{}')".format(name,phone,email,addr,passw)
    cur.execute(s)
    cn.commit()
    cn.close()
    return

def pmenu(x):
    b=("Cuisine no", "Cuisine", "Price")
    print(b)
    print()
    for a in x:
        print(a)
    print()
    print()
    return

def menu():
    if choice2==1:
        print("The SOUP items are as follows: ")
        print()
        x=soup
        pmenu(x)
    elif choice2==2:
        print("The SALAD items are as follows: ")
        print()
        x=salad
        pmenu(x)
    elif choice2==3:
        print("The MINI PLATE items are as follows: ")
        print()
        x=mini
        pmenu(x)
    elif choice2==4:
        print("The APPETIZER items are as follows: ")
        print()
        x=appe
        pmenu(x)
    elif choice2==5:
        print("The PASTA items are as follows: ")
        print()
        x=pasta
        pmenu(x)
    elif choice2==6:
        print("The BURGER items are as follows: ")
        print()
        x=burger
        pmenu(x)
    elif choice2==7:
        print("The SANDWITCH items are as follows: ")
        print()
        x=sand
        pmenu(x)
    elif choice2==8:
        print("The PIZZA items are as follows: ")
        print()
        x=pizza
        pmenu(x)
    elif choice2==9:
        print("The MAIN items are as follows: ")
        print()
        x=main
        pmenu(x)
    elif choice2==10:
        print("The RICE and NOODLES items are as follows: ")
        print()
        x=rnn
        pmenu(x)
    elif choice2==11:
        print("The BREAD items are as follows: ")
        print()
        x=bread
        pmenu(x)
    elif choice2==12:
        print("The DESSERT items are as follows: ")
        print()
        x=dess
        pmenu(x)
    elif choice2==13:
        print("The SHAKE items are as follows: ")
        print()
        x=shake
        pmenu(x)
    elif choice2==14:
        print("The SMOOTHIE items are as follows: ")
        print()
        x=smoo
        pmenu(x)
    elif choice2==15:
        print("The COOLER items are as follows: ")
        print()
        x=cool
        pmenu(x)
    elif choice2==16:
        print("The TEA items are as follows: ")
        print()
        x=tea
        pmenu(x)
    elif choice2==17:
        print("The COFFEE items are as follows: ")
        print()
        x=coffee
        pmenu(x)
    return

print()
choice1=input("Are you a new costumer? (yes/no) ")
print()
coun=0
if choice1=="yes":
    regis()
else:
    while coun==0:
        print("Please enter the following details for logging into your account")
        print()
        print("Enter 1 for logging in with phone number")
        print("Enter 2 for logging in with email")
        choice2=int(input("Enter choice: "))
        print()
        if choice2==1:
            phone=int(input("Phone number: "))
            passw=input("Password: ")
            print()
            cn=c.connect(host='localhost',user='root',passwd='',database='mak')
            cur=cn.cursor()
            cur.execute("select * from regis")
            data=cur.fetchall()
            cn.close()
            for x in data:
                if x[1]==phone:
                    d=x
                    if d[4]==passw:
                        name=d[0]
                        email=d[2]
                        coun=1
                    else:
                        print("The password entered is wrong")
                        print()
                    coun1=1
                    break
                else:
                    coun1=0
            if coun1==0:
                print("No account registered with this number")
                print()
                regis()
                coun=1
        else:
            email=input("Email: ")  
            passw=input("Password: ")
            print()
            cn=c.connect(host='localhost',user='root',passwd='',database='mak')
            cur=cn.cursor()
            cur.execute("select * from regis")
            data=cur.fetchall()
            cn.close()
            for x in data:
                if x[2]==email:
                    d=x
                    if d[4]==passw:
                        name=d[0]
                        phone=d[1]
                        coun=1
                    else:
                        print("The password entered is wrong")
                        print()
                    coun1=1
                    break
                else:
                    coun1=0
            if coun1==0:
                print("No account registered with this number")
                print()
                regis()
                coun=1

print("THANK YOU",name+",","You have successfully logged into your account")
print()
x=input("Please press enter to proceed.")
print()
x=input("Our cafe offers a large variety of cuisines from across the world")
print()
print("The MENU is as follows: ")
print()
print("1: SOUPS")
print("2: SALADS")
print("3: MINI PLATES")
print("4: APPETIZERS")
print("5: PASTA")
print("6: BURGER")
print("7: SANDWICH")
print("8: PIZZA")
print("9: MAINS")
print("10: RICE and NOODLES")
print("11: BREADS")
print("12: DESSERTS")
print("13: SHAKES")
print("14: SMOOTHIES")
print("15: COOLERS")
print("16: TEA")
print("17: COFFEE")
print()
print()
print("Enter item number for the sub menu")
print("Press 0 for placing an order")
print()
print()

cn=c.connect(host="localhost",user="root",passwd="")
cur=cn.cursor()
pno=str(phone)
datab="mak"+pno
b="create database if not exists "
co=b+datab
cur.execute(co)
cn.close()

cn=c.connect(host="localhost",user="root",passwd="",database=datab)
cur=cn.cursor()
cur.execute("show tables")
data1=cur.fetchall()
cou=cur.rowcount
cou=cou+1
cou1=str(cou)
u="order"
x="create table order"
y="(cno integer primary key,cname char(30),amount integer, price integer, tprice integer)"
z=x+cou1+y
cur.execute(z)
table=u+cou1
cn.close()

cn=c.connect(host='localhost',user='root',passwd='',database='mak')
cur=cn.cursor()
cur.execute("select * from menu")
soup=cur.fetchmany(5)
salad=cur.fetchmany(6)
mini=cur.fetchmany(8)
appe=cur.fetchmany(12)
pasta=cur.fetchmany(7)
burger=cur.fetchmany(4)
sand=cur.fetchmany(4)
pizza=cur.fetchmany(4)
main=cur.fetchmany(6)
rnn=cur.fetchmany(6)
bread=cur.fetchmany(7)
dess=cur.fetchmany(5)
shake=cur.fetchmany(7)
smoo=cur.fetchmany(5)
cool=cur.fetchmany(10)
tea=cur.fetchmany(3)
coffee=cur.fetchmany(8)
cn.close()

while True:
    choice2=int(input("Enter choice: "))
    print()
    print()
    if choice2==0:
        print("Enter the cuisine number for ordering the item.")
        print("Enter 0 for placing the order.")
        print()
        while True:
            ch=int(input("Enter cuisine number: "))
            if ch==0:
                print("thank you")
                break
            else:
                am=int(input("Enter quantity: "))
                print()
                cn=c.connect(host="localhost",user="root",passwd="",database="mak")
                cur=cn.cursor()
                cur.execute("select * from menu")
                d=cur.fetchall()
                for x in d:
                    if x[0]==ch:
                        item=x
                cn.close()
                
                cn=c.connect(host="localhost",user="root",passwd="",database=datab)
                cur=cn.cursor()
                cno=item[0]
                cname=item[1]
                cpr=item[2]
                tpr=cpr*am
                x="insert into "
                y=" values({},'{}',{},{},{})"
                z=x+table+y
                cur.execute(z.format(cno,cname,am,cpr,tpr))
                cn.commit()
                cn.close()
        break
    else:
        menu()

cn=c.connect(host="localhost",user="root",passwd="",database=datab)
cur=cn.cursor()
x=("cuisine number","cuisine","amount","price","total")
print(x)
print()
x="select * from "
y=x+table
cur.execute(y)
data3=cur.fetchall()
tpr=0
for x in data3:
    print(x)
    tpr=tpr+x[4]
cn.close()
print()
print("The total amount is",tpr)
        











