prices = [3,3,5,0,0,3,1,4]
buy = 0
sell = 0
profit= []

i = 0 
while i <len(prices)-1:
    print(buy,"buy")
    print(sell,"sell")
    print(i,"i")
    print(i+1,"i+1" )
    print(profit,"profit")
    if prices[i+1] < prices[i]:
        if prices[sell] > prices[buy]:
            print("aoifhaoihfoa")
            print(len(profit),"len profit")
            if len(profit) == 2 :
                print("iafioahfoiahfoiahf")
                min = min(profit)
                print(min,"min")
                profit.pop(min)
                print(profit,"after pop")
                profit.append(prices[sell]-prices[buy])
                print(profit,"after append")
            else:
                profit.append(prices[sell]-prices[buy])
                
        buy = i+1
        sell = i +1
    else:
        if prices[i+1] > prices[sell]:
            sell = i+1
    
    i += 1
if len(profit) == 2 :
    print("iafioahfoiahfoiahf,2")
    print(profit,"profit")
    min = min(profit)
    print(min,"min")
    ind = profit.index(min)
    profit.pop(ind)
    print(profit,"after pop")
    profit.append(prices[sell]-prices[buy])
    print(profit,"after append")
else:
    profit.append(prices[sell]-prices[buy])

print(profit)

print(sum(profit[:2]))
