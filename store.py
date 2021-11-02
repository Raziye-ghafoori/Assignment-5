import csv
Products=[]
def laod_data():
    print("pleas wait....")
    file=open("database.csv",'r')
    for row in file:
        info=row[:-1].split(',')
        temp_dec={"code":info[0],"name":info[1],"price":info[2],"number":info[3]}
        Products.append(temp_dec)
    print("Ok Goo!!!!")

def show_meno():
    print("wellcom to my stor::")
    print('1.Add')
    print('2.Edit')
    print('3.Delete')
    print('4.Show List')
    print('5.Search')
    print('6.Buy')
    print('7.Save and Exit')

def Add():
    name=input("enter name of Product::")
    for i in Products:
        if name == i['name']:
            print("the product is available!!")
            return
    code=input("enter code of Product::")
    price=input("enter price of Product::")
    number=input("enter number of Product::")
    Products.append({"code":code,"name":name,"price":price,"number":number})
    print("Ok!! ADDED")

def Edit(pro):
    while True:
        for i in Products:
            if pro == i['name']:
                a=input("enter the new price:: ")
                i['price']=a
                print("OK!!!! The price changed")
                return
        print("opss!! I can\'t find\n enter again::")
        pro=input()
    
def Delete(pro):
    for i in  Products:
        if i["name"] == pro:
            Products.remove(i)
            print("Removed successfully!!!!")
            return
    print("This Product not available!!!")      

def Show_List():
    print("Code\tName\tPrice\tNumber")
    for product in Products:
        print (product["code"],'\t',product["name"],'\t',product["price"],'\t',product["number"])

def Search(pro):
    for i in Products:
        if pro == i['name']:
            print(i) 
            return True  

    print("Opss!😅! I can\'t find!!")
    return False
    
def Buy(pro):
    for i in Products:
        if pro == i['name']:
            a=int(i["number"])
            if a==0:
                Delete(pro)
                break
            else:
                print("💰pleas deposit money!!!!💰")
                a-=1
                i["number"]=a
                print("Do not need anything else???")
                return
    print("We have no inventory!!!\n sorry😕")
    
def Save_and_Exit():
    list=['','','','']
    file=open("database.csv",'w')
    writer = csv.writer(file)
    for pro in Products:
        list[0]=pro["code"]
        list[1]=pro["name"]
        list[2]=pro["price"]
        list[3]=pro["number"]
        writer.writerow(list) 
    file.close()
    print("🙋Your Wellcome🙋")
    exit()
        
laod_data()
while True :
    show_meno()
    choice=int(input("Enter your choice::"))
    if choice==1:
        Add()
    elif choice==2:
        pro=input("enter the product you want:")
        Edit(pro)
    elif choice==3:
        pro=input("enter the product you want:")
        Delete(pro)
    elif choice==4:
        Show_List()
    elif choice==5:
        pro=input("enter the product you want:")
        Search(pro)
    elif choice==6:
        pro=input("enter the product you want:")
        Buy(pro)
    elif choice==7:
        Save_and_Exit()

    

    