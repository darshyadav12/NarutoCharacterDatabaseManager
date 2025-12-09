import mysql.connector as my_sql
# Function to create database and table
def Create():
    mydb=my_sql.connect(host='localhost',user='root',password='qwert')
    cur=mydb.cursor()
    cur.execute('create database NarutoCharacters')
    cur.execute('use NarutoCharacters')
    cur.execute('create table Characters(Sno int(10) primary key, Name Varchar(20), Village varchar(20), Clan varchar(20),Chakra_Type varchar(30),Summoning_Animal varchar(20),Ninja_Rank varchar(15))')
    mydb.close()
# Function to add row information
def Insert():
    mydb=my_sql.connect(host='localhost',user='root',password='qwert',database='NarutoCharacters')
    cur=mydb.cursor()
    n= int(input('Enter total number of Character'))
    for i in range(n):
        Sno=int(input('Enter Character No:'))
        name=input('Enter Name:')
        V= input('Enter Village: ')
        S=input('Enter Clan: ')
        P= input('Enter Chakra_Type:')
        T=input('Enter Summoning_Animal:')
        E=input('Enter Ninja_Rank:-')
        ins="insert into Characters values(%s,'%s','%s','%s','%s','%s','%s')"%(Sno,name,V,S,P,T,E)
        cur.execute(ins)
    mydb.commit()
    mydb.close()
# Functions to display data values
def Display():
    mydb=my_sql.connect(host='localhost',user='root',password='qwert',database='NarutoCharacters')
    cur = mydb.cursor()
    cur.execute("select * from Characters")
    print('________________________________________________________________________________________________________________________')
    print('Sno\tName\tVillage\tClan\tChakra_Type\tSummoning_Animal\tNinja_Rank\n')
    print('________________________________________________________________________________________________________________________')
    for row in cur:
        print(row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t',row[4],'\t',row[5],'\t',row[6])
    mydb.close()
def DisplayVillage():
    mydb=my_sql.connect(host='localhost',user='root',password='qwert',database='NarutoCharacters')
    cur = mydb.cursor()
    ver=input('enter Village')
    cur.execute("select * from Characters where Village='%s'"%(ver))
    print("________________________________________________________________________________________________________________________")
    print('Sno\tName\tVillage\tClan\tChakra_Type\tSummoning_Animal\tNinja_Rank\n')
    print("________________________________________________________________________________________________________________________")
    for row in cur:
        print(row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t',row[4],'\t',row[5],'\t',row[6])
    mydb.close()
def displayname():
    mydb=my_sql.connect(host="localhost",user="root",password="qwert",database="NarutoCharacters")
    cur = mydb.cursor()
    name=input("enter name")
    cur.execute("select * from Characters where name='%s'"%(name))
    print("________________________________________________________________________________________________________________________")
    print('Sno\tName\tVillage\tClan\tChakra_Type\tSummoning_Animal\tNinja_Rank\n')
    print("________________________________________________________________________________________________________________________")
    for row in cur:
        print(row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t',row[4],'\t',row[5],'\t',row[6])
    mydb.close()
def displayclan():
    mydb=my_sql.connect(host="localhost",user="root",password="qwert",database="NarutoCharacters")
    cur = mydb.cursor()
    g=input("enter any clan")
    cur.execute("select * from Characters where clan='%s'"%(g))
    print("________________________________________________________________________________________________________________________")
    print('Sno\tName\tVillage\tClan\tChakra_Type\tSummoning_Animal\tNinja_Rank\n')
    print("________________________________________________________________________________________________________________________")
    for row in cur:
        print(row[0],'\t\t',row[1],'\t',row[2],'\t\t\t',row[3],'\t\t\t',row[4],'\t\t\t',row[5],'\t\t\t',row[6])
    mydb.close()
# Function to modify data values
def updatename():
    mydb=my_sql.connect(host="localhost",user="root",password="qwert",database="NarutoCharacters")
    cur = mydb.cursor()
    n=input("Enter any name")
    m=int(input("Enter any sno"))
    ins = "update Characters set name='%s' where sno='%s'"%(n,m)
    cur.execute(ins)
    mydb.commit()
    mydb.close()
def updateVillage():
    mydb=my_sql.connect(host="localhost",user="root",password="qwert",database="NarutoCharacters")
    cur = mydb.cursor()
    s=input("Enter any Village")
    m=int(input("Enter any sno"))
    ins = "update Characters set Village='%s' where sno='%s'"%(s,m)
    cur.execute(ins)
    mydb.commit()
    mydb.close()
def updateClan():
    mydb=my_sql.connect(host="localhost",user="root",password="qwert",database="NarutoCharacters")
    cur = mydb.cursor()
    n=input("Enter any Clan")
    m=int(input("Enter any sno"))
    ins = "update Characters set Clan='%s' where sno='%s'"%(n,m)
    cur.execute(ins)
    mydb.commit()
    mydb.close()
def updateChakra_Type():
    mydb=my_sql.connect(host="localhost",user="root",password="qwert",database="NarutoCharacters")
    cur = mydb.cursor()
    g=input("Enter any Chakra_Type")
    m=int(input("Enter any sno"))
    ins = "update Characters set Chakra_Type='%s' where sno='%s'"%(g,m)
    cur.execute(ins)
    mydb.commit()
    mydb.close()
def updatetSummoning_Animal():
    mydb=my_sql.connect(host="localhost",user="root",password="qwert",database="NarutoCharacters")
    cur = mydb.cursor()
    g=input("Enter any Summoning_Animal")
    m=int(input("Enter any sno"))
    ins = "update Characters set Summoning_Animal='%s' where sno='%s'"%(g,m)
    cur.execute(ins)
    mydb.commit()
    mydb.close()
def updatetNinja_Rank():
    mydb=my_sql.connect(host="localhost",user="root",password="qwert",database="NarutoCharacters")
    cur = mydb.cursor()
    g=input("Enter any Ninja_Rank")
    m=int(input("Enter any sno"))
    ins = "update Characters set Ninja_Rank='%s' where sno='%s'"%(g,m)
    cur.execute(ins)
    mydb.commit()
    mydb.close()
# Functions to remove row information
def deletename():
    mydb=my_sql.connect(host="localhost",user="root",password="qwert",database="NarutoCharacters")
    cur = mydb.cursor()
    n=input("Enter any name")
    ins = "delete from Characters where name='%s'"%(n)
    cur.execute(ins)
    mydb.commit()
    mydb.close()
#Main Program
ch="y"
while ch=="Y" or ch=="y":
    print("1: Create\n\n2:Insert\n\n3:Display\n\n4:Update\n\n5.Delete\n\n6.Exit")
    c=int(input("Enter your Choice"))
    if c==1:
        Create()
    elif c==2:
        Insert()
    elif c==3:
        print("1:Full Table Info\n\n2:DisplayVillage\n\n3:Display Name\n\n4:Display Clan")
        ch=int(input("Enter your Choice"))
        if ch==1:
            Display()
        elif ch==2:
            DisplayVillage()
        elif ch==3:
            displayname()
        elif ch==4:
            displayclan()
        else:
            print("Wrong Input")
    elif c==4:
        print("1: update name \n\n2:update Village\n\n3. update Clan\\n\n4. update Chakra_Type\\n\n5. update Summoning_Animal\\n\n6. update Ninja_Rank ")
        ch=int(input("Enter your Choice"))
        if ch==1:
            updatename()
        elif ch==2:
            updateVillage()
        elif ch==3:
            updateClan()
        elif ch==4:
            updateChakra_Type()
        elif ch==5:
            updatetSummoning_Animal()
        elif ch==6:
            updatetNinja_Rank()
    elif c==5:
        deletename()
    else:
        break
    ch=input("Do you want to continue or not[Y/N]")
