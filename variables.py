import math

# A school garden is 12 meters long and 8 meters wide.
# Calculate the area of the garden.
l = 12
b = 8
A = l * b
print("The area of the garden is", A, "square meters.")  # 96

# A round table has a radius of 5 meters. Calculate the area of the table's surface.
r = 5
A = math.pi * r**2
print("The area of the table's surface is", A, "square meters.")  # ~78.53981633974483

# A triangular billboard has a base of 10 meters and a height of 6 meters. Calculate its area.
b_tri = 10
h = 6
A = 0.5 * b_tri * h
print("The area of the triangular billboard is", A, "square meters.")  # 30.0

# A square tile has sides of 9 cm. Calculate the area of one tile.
s = 9
A = s**2
print("The area of one tile is", A, "square centimeters.")  # 81


#A playground is made up of:
#a rectangle: 20 m by 15 m
#a semicircle attached to one side with radius 10 m
#calculate the total area of the playground.

L = 20
W = 15
A_rectangle = L * W
r = 10
A_semicircle = 0.5 * math.pi * r**2
total_area = A_rectangle + A_semicircle
print("The area of the rectangle is", A_rectangle, "square meters.")  # 300
print("The area of the semicircle is", A_semicircle, "square meters.")  # ~157.07963267948966
print("The total area of the playground is", total_area, "square meters.")  # ~457.07963267948966