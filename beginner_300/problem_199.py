ohlc = [["open",'high','low','close'],[100,110,70,100],[200,210,180,190],[300,310,300,310]]
for i in ohlc[1:]:
    if i[3]>i[0]:
        print(i[1]-i[2])
