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
amount_paid = float(input(“How much did you pay?: ”))
cost = float(input(“How much did it cost?: ”))
change = amount_paid - cost
print(“Change is:”, change)
change *= 100
num_quarters = change // 25
change -= (num_quarters*25)
num_dimes = change // 10
change -= (num_dimes*10)
num_pennies = change

print(“Num quarters is:”, num_quarters)
print(“Num dimes is:”, num_dimes)
print(“Num pennies is:”, num_pennies)
