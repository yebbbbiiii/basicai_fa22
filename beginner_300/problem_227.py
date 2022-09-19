def print_mxn(string):
    len3 = int(len(string)/3)
    for i in range(len3 +1):
        print(string[i*3:i*3+3])
        
print_mxn("아이엠어보이유알어걸")