'''
A computer program analyses the price of a product in an online store. If the product price decreases by at least 10%, the program prints a purchase recommendation:

Buy the product!!
Product price reduced by 17%

Create such program. The current and previous price of the product are included in variables. Sample result:

Current product price: 140.00
Previous product price: 200.00
Buy the product!!
Product price reduced by 30%
'''

currentprice=140
previousprice=200
pricereduce=round((1-(currentprice/previousprice))*100)
print(pricereduce)

print(f'current price: {currentprice:.2f}')
print(f'previous price: {previousprice:.2f}')

if pricereduce>=10:
    print('buy the product!!')
    print(f'price reduced by {pricereduce} %')
else:
    print('no need to rush')
    print(f'price reduced by {pricereduce} %')
