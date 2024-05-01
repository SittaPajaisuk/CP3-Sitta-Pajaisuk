menuList = []
priceList = []
total = 0

while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit"):
        break

    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)

    for i in range(len(priceList)):
        total = total + (int(priceList[i]))




def showBill():
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
    print("total",total ,"THB")

showBill()
