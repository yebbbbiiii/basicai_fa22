result = []
data = [[2000,3050,2050,1980],[7500,2050,2050,1980],[15450,15050,15550,14900]]
for i in data:
    for k in i:
        result.append(k*1.00014)
print(result)