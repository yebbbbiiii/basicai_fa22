class Stock:
    def __init__(self,name,code):
        self.name = name
        self.code = code
    
    def set_name(self,name):
        self.name = name
        
    def set_code(self,code):
        self.code = code
        
    def get_name(self,name):
        return self.name
            
    def get_code(self,code):
        return self.code
        
a = Stock("삼성전자","005930")
print(a.name)
print(a.code)
print(a.get_code())
print(a.get_code())