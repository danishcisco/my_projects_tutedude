"""
calculate area of triangle, where all side of the the triangle is know
Let the side lengths be ( a ), ( b ), and ( c ).
Calculate the semi-perimeter: (s) = (a + b + c) / 2
Calculate the area: = square root of (s * (s - a) * (s - b) * (s - c))
Any number to the power of half is called square root
"""

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))
s = (a+b+c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("Area of triangle: ", round(area, 2))

