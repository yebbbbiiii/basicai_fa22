def print_5xn(string):
    len5 = int(len(string)/5)
    for i in range(len5 +1):
        print(string[i*5:i*5+5])
        
print_5xn("아이엠어보이유알어걸")