warn_investment_list = ["Microsoft","Google","Naver","Kakao","SAMSUNG","LG"]
user = input("투자 종목은?")
if user in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")