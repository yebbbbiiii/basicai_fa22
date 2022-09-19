class Stock:
    def __init__(self,name,code,per,pbr,배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률
    
    def set_name(self,name):
        self.name = name
        
    def set_code(self,code):
        self.code = code
        
    def get_name(self):
        return self.name
            
    def get_code(self):
        return self.code
    
    def set_per(self,per):
        self.per = per
        
    def get_pbr(self,pbr):
        self.pbr = pbr
            
    def get_dividend(self,배당수익률):
        self.배당수익률 = 배당수익률
종목 = [] 
     
삼성 = Stock("삼성전자","005930",15.79,1.33,2.83)
현대차 = Stock("현대차","005380",8.70,0.35,4.27)
LG전자 = Stock("LG전자","066570",317.34,0.69,1.37)

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code,i.per)
