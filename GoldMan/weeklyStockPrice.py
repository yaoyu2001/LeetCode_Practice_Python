def weeklyStockPrice(dailyPrice):
    res = list()
    length = len(dailyPrice)
    if length < 7:
        return res

    prefixSum = [0]*(length+1)
    for i in range(1,length + 1):
        prefixSum[i] = prefixSum[i-1] + dailyPrice[i-1]
    for i in range(7, len(prefixSum)):
        avg = (prefixSum[i] - prefixSum[i-7])/7
        res.append(str(round(avg,2)))
    return res

dailyPrice = [7,8,8,11,9,7,5,6]

print(weeklyStockPrice(dailyPrice))