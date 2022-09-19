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

삼성 = Stock("삼성전자","005930",15.79,1.33,2.83)
삼성.set_per(12.75)
print(삼성.per)
