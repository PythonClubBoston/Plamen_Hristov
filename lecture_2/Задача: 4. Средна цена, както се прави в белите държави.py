prices = []
averagePrice = 0.0
while True:
    price = input('Please add price: ')
    if(price == 'stop'):
        for price in prices:
            averagePrice += float(price)
        averagePrice = averagePrice/len(prices)
        print(averagePrice)
        break
    else:
        prices.append(price)

