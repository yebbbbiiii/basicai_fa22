user = input("휴대전화번호를 입력하세요")
first_num = user.split("-")[0]
if first_num == "011":
    print("당신은 SKT 사용자입니다")
elif first_num == "016":
    print("당신은 KT 사용자입니다")
elif first_num == "019":
    print("당신은 LGU사용자입니다")
elif first_num == "010":
    print("당신은 알수없는 사용자입니다")