def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice * 7 / 100)
    return result
userInput = int(input("Enter Total Price : "))
print(vatCalculate(userInput))
