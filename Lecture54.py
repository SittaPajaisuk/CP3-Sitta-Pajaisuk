def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("Done !")
        return showMenu()
    else:
        print("Incorrect")

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        print(vatCalculator(int(input("Vat : " ))))
    elif userSelected == 2:
        print(priceCalculator())

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

login()