phone_book=[]

def add():
    name=input("name:")
    phone=input("phone number")
    name_phone={"name":name,"phone":phone}
    phone_book.append(name_phone)
    print(name_phone["name"])
    print("新增成功")

def find():
    name = input("name(按enter跳過):")
    phone = input("phone number(按enter跳過):")
    result=[]
    for name_phone in phone_book:
        if (name_phone["name"]==name or name_phone["phone"]==phone):
            result.append(name_phone)
            print(result)

def print_all():
    for name_phone in phone_book:
        print("name:",name_phone["name"],"/ phone number:",name_phone["phone"])
a=0
while a<1:
    print("1:add(name, phone)")
    print("2:find(name, phone)")
    print("3:print all")
    print("4:finish")
    action=input("choose the number")
    action=int(action)
    if action==1:
        add()
    elif action==2:
        find()
    elif action==3:
        print_all()
    elif action==4:
        break
    else:
        print("重新輸入")




