volatility = []
low = [100,200,400,800,1000]
high = [150,300,430,880,1000]
for i in range(len(low)):
    volatility.append(high[i]-low[i])
    print(volatility)