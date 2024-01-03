num = int(input(""))
text = 0
for i in range(num):
    print(" " * (num - i) + "*" * (text+1))
    text += 2