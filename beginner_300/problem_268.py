class Stock:
    def __init__(self,name,code,per,pbr,dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend =dividend
    
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
            
    def get_dividend(self,dividend):
        self.dividend = dividend