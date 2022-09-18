user = input("영어를 입력하세요(대소문 상관 없음) : ")
user1 = user.islower()
if user1 == True:
    print(user.upper())
else:
    print(user.lower())