주민등록번호 = input("주민등록번호:")
주민등록번호 = 주민등록번호.split("-")[1]
if 주민등록번호[0] ==1 or 주민등록번호[0] ==3:
    print("남자")
else:
    print("여자")