from binascii import b2a_base64


환율 = {"달러" :1167,"엔":1.096, "유로":1268,"위안":171}
user = input("입력: ")
a,b = user.split()
print(float(a)*환율[b],"원")