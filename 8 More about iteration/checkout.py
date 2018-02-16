#Checkout
#Print total price, total items, average price of each product

"""There is still a bug where if you input 0, -8, 0 you encounter the bug. As of right now I don't know how to fix it."""

price=1
counter=0
total_price=0

while(price != 0):
    price=input("Item Price (0 when done): ")           #Ask for input
    price=int(price)

    while (counter == 0 and price == 0):                                            #For no items
        print("Can't compute an average without any items.")
        price=input("Item Price (0 when done): ")
        price=int(price)

    while (price < 0):                                                          #For negative numbers
        print("Error. Price can't be negative.")
        price=input("Item Price (0 when done): ")
        price=int(price)

    counter += 1
    total_price= total_price+price


counter -= 1

average = total_price/counter

print("Total Price: ", "%.2f" % total_price)
print("Item Count: ", counter)
print("Average Item Price: ", "%.2f" % average)

#print("%.2f" % a)                                                      #Formatting
