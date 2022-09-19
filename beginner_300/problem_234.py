def pickup_even(짝수):
    리스트 = []
    for 변수 in 짝수:
        if 변수 %2 ==0:
            리스트.append(변수)
    print(리스트)
    
pickup_even([3,4,5,6,7,8])