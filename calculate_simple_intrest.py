"""
The formula for simple interest is:
SI = (P * R * T) / 100
Where:
P = Principal amount (initial money)
R = Rate of interest (per year, in %)
T = Time period (in years)
Total amount after interest:
A = P + SI
"""

p = float(input("Enter the principle amount: "))
r = float(input("Enter the rate of intrest: "))
t = float(input("Enter the tenure: "))

si = (p * r * t) / 100
A = p + si
print("Simple Intrest Amount: ", si)
print("Total Amount: ", A)