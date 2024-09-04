# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Nivriti Eadala
# Robin El Attar
# Nithya Vemuri
# Mirthvika Srinivasan
# Section: 505
# Assignment: 4.15 - Make Change
# Date: 04 September 2024
# 


amount_paid = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
change = amount_paid - cost
print(f'You received ${change:.2f} in change. That is...')
change *= 100
change = round(change, 2)
#Calculate number of coins needed for change
num_quarters = 0
num_dimes = 0
num_nickels = 0
num_pennies = 0
if(change>=25):
    num_quarters = int(change // 25)
    change -= (num_quarters*25)
if(change >= 10):
    num_dimes = int(change // 10)
    change -= (num_dimes*10)
if(change >= 5):
    num_nickels = int(change // 5)
    change -= (num_dimes*5)
if(change >= 1):
    num_pennies = int(change)


#Depending on the amount of change, the output will change to fit the situation
if(num_quarters > 0):
    if(num_quarters == 1):
        print(f'{num_quarters} quarter')
    else:
        print(f'{num_quarters} quarters')
if(num_dimes > 0):
    if(num_dimes == 1):
        print(f'{num_dimes} dime')
    else:
        print(f'{num_dimes} dimes')
if(num_nickels > 0):
    if(num_nickels == 1):
        print(f'{num_nickels} nickel')
    else:
        print(f'{num_nickels} nickles')
if(num_pennies > 0): 
    if(num_pennies == 1):
        print(f'{num_pennies} penny')
    else:
        print(f'{num_pennies} pennies')
