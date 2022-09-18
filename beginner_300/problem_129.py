num = input("주민등록번호:")
단계1 = int(num[0])*2 +  int(num[1])*3 +int(num[2])*4 +int(num[3])*5 +int(num[4])*6 +int(num[5])*7 +int(num[7])*8 +int(num[8])*2 +int(num[10])*3 +int(num[11])*4 +int(num[12])*5
단계2 = 11-(단계1%11)
단계3 = str(단계2)

if num[-1] == 단계3[-1]:
    print("유효한 주민등록번호입니다")
else:
    print("유효하지않은 주민등록번호입니다")