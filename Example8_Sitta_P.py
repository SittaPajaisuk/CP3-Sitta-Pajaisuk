usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput  == "attis"  and passwordInput == "1313":
    print("Successful !")
    print("-------- Welcome",usernameInput," To Winnter-Shop --------")
    print("1. Coat 1,200 THB")
    print("2. Jacket 1,399 THB")
    print("3. Sweater 990 THB")
    print("4. Shirt 799 THB")
    print("5. T-Shirt 390 THB")
    print("6. Hoodie 699 THB")
    print("------------------------------------------------")
    userSelected = int(input("Choose products >> "))
    print("------------------------------------------------")
    if userSelected == 1:
        print("Coat 1,200 THB")
        number = int(input("Choose Number of products >> "))
        products = "Coat"
        Product_price = 1200
    elif userSelected == 2:
        print("Jacket 1,399 THB")
        number = int(input("Choose Number of products >> "))
        products = "Jaket"
        Product_price = 1399
    elif userSelected == 3:
        print("Sweater 990 THB")
        number = int(input("Choose Number of products >> "))
        products = "Sweater"
        Product_price = 990
    elif userSelected == 4:
        print("Shirt 799 THB")
        number = int(input("Choose Number of products >> "))
        products = "Shirt"
        Product_price = 799
    elif userSelected == 5:
        print("T-Shirt 390 THB")
        number = int(input("Choose Number of products >> "))
        products = "T-Shirt"
        Product_price = 390
    elif userSelected == 6:
        print("Hoodie 699 THB")
        number = int(input("Choose Number of products >> "))
        products = "Hoodie"
        Product_price = 699
    print("------------------------------------------------")
    print("Total")
    print("------------------------------------------------")
    print("", products,"x", number, "=", "{:,}".format(Product_price * number)," THB")
    print("------------------------------------------------")
    print("THANK YOU")


