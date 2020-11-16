#The purpose of this code was to write a program with total change amount as an integer input, 
#and output the change using the fewest coins, one coin type per line. 
#The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. 
#Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

remainingChange = 0
change = []
moneyNames = ["Dollar","Dollars","Quarter","Quarters","Dime","Dimes","Nickel","Nickels","Penny","Pennies"]
currency = [100, 25, 10, 5, 0]
counter = 0
#Get user input
providedNumber = int(input('Enter a integer: '))
#Loop through and get change
for x in currency:
    counter += 1
    if counter <= 1:
        remainingChange = providedNumber % x
        change.insert(counter - 1, providedNumber // x)
    else:
        if remainingChange > x and x >= 5:
            change.insert(counter - 1, remainingChange // x)
            remainingChange = remainingChange % x
        elif remainingChange < 5 and x == 0:
            change.insert(counter - 1, remainingChange)
        else:
            change.insert(counter - 1, 0)
print("Your change is ")
counter = 0
for i in change:
    if i == 1:
        print(i, moneyNames[counter])
    else:
        print(i, moneyNames[counter + 1])
    counter += 2
