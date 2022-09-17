user = int(input("입력값:"))
hap = user -20
if hap < 0:
    print("0")
elif hap>255:
    print(255)
else:
    print(hap)
   