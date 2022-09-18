user1 = int(input("첫번째 숫자를 입력하세요:"))
user2 = int(input("두번째 숫자를 입력하세요:"))
user3 = int(input("세번째 숫자를 입력하세요:"))

if user1>= user2 and user1 >= user3:
    print(user1)
elif user2>=user1 and user2>= user3:
    print(user2)
elif user3>=user1 and user3>=user2:
    print(user3)