'''
In one of the online stores, a 25% discount is charged for each product purchased over two. Write a program that calculates the amount to be paid.
 Read the number of purchased products and the product price from the keyboard. Sample result:

Number of products purchased: 5
Product price: 40
Amount to pay: 170.00
'''

products_bought=5
price=40
total_price=0

for i in range(1,products_bought+1):
    if i>2:
        total_price=total_price+price*0.75
    else:
        total_price=total_price+price
print(total_price)
