def login():
  usernameInput = input("Username : ")
  passwordInput = input("Password : ")
  if usernameInput == "admin" and passwordInput == "1234":
    print("Done!!!")
    showMenu()
  else:
    print("Wrong!!!")
    login()
  
def showMenu():
  print("----- iShop -----")
  print("1. Vat Calculator")
  print("2. Price Calculator")
  menuSelect()

def menuSelect():
  userSelected = int(input(">>"))
  if userSelected == 1:
    print("Total Price :",vatCalculate(int(input("Price (THB) : "))))
  elif userSelected == 2:
    print("Total Price :",pricecalcuate())

def vatCalculate(totalPrice):
  vat = 7
  result = totalPrice + (totalPrice * vat / 100)
  return result
  
def pricecalcuate():
  price1 = int(input("First Product Price : "))
  price2 = int(input("Second Product Price : "))
  return vatCalculate(price1 + price2)

login()
