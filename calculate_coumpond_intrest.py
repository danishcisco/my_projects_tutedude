"""
The formula to calculate compound interest is:
A = P (1 + R/100) ^ T
Where:
A = final amount (principal + interest)
P = principal (initial amount)
R = annual interest rate (in %)
T = time (in years)
Then the compound interest (CI) is:
CI = A - P
"""

p = float(input("Enter the principle amount: "))
r = float(input("Enter the rate of intrest: "))
t = float(input("Enter the tenure: "))
amount = p * (1 + r/100) ** t
ci = amount - p

print("Total Amount: ", round(amount, 2))
print("Compound Intrest Amount: ", round(ci, 2))
