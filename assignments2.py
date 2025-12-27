print("question 1")
# Given:
a = "12"
b = 7.5
c = 3

# Tasks:
# Convert a to an integer
# Add all three values
# Multiply the result by 2
# Print the final result and its data type

# answer
a = int(a)
result = a + b + c
final_result = result * 2
print(final_result)
print(type(final_result))


print("question 2")
# A student scored:
# 78 in Math (string)
# 85.5 in Science (string)
# 69 in English (integer)
math = "78"
science = "85.5"
english = 69

# Tasks:
# Convert all scores to numeric values
# Calculate the total score
# Calculate the average score
# Print both values and their data types

# answer
math = int(math)
science = float(science)
total = math + science + english
average = total / 3
print("Total score:", total)
print("Type of total:", type(total))
print("Average score:", average)
print("Type of average:", type(average))


print("question 3")
# A worker earns a monthly salary of ₵3,200.
# Rent takes 30%
# Transport takes 12.5%
# Food takes 20%
salary = "3200"
rent_rate = 0.30
transport_rate = 0.125
food_rate = 0.20

# Tasks:
# Convert salary to an integer
# Calculate how much is spent on each expense
# Calculate the remaining balance
# Print all results clearly with their data types

# answer
salary = "3200"
rent_rate = 0.30
transport_rate = 0.125
food_rate = 0.20
salary = int(salary)
rent = salary * rent_rate
transport = salary * transport_rate
food = salary * food_rate
balance = salary - (rent + transport + food)
print("Salary:", salary, type(salary))
print("Rent expense:", rent, type(rent))
print("Transport expense:", transport, type(transport))
print("Food expense:", food, type(food))
print("Remaining balance:", balance, type(balance))


print("question 4")
# A rectangular field has:
Length = "18.5" 
Width = "12"
length = "18.5"
width = "12"

# Tasks:
# Convert both values correctly
# Calculate the area
# Multiply the area by 1.75 (cost per square meter)
# Print the final cost and its data type

# answer
length = float(length)
width = int(width)
area = length * width
final_cost = area * 1.75
print("Final cost:", final_cost)
print("Data type:", type(final_cost))


print("question 5")
# Given:
x = 4 + 3j
y = "2"

# Tasks:
# Convert y to an integer
# Add y to x
# Multiply the result by 2
# Print the final value and its data type

# answer
y = int(y)
result = x + y
final_value = result * 2
print(final_value)
print(type(final_value))


print("question 6")
# Given:
num = 50

# Tasks:
# Convert num to float
# Convert the float to string
# Convert the string back to integer
# Print each value and its data type at every step

# answer
num_float = float(num)
print(num_float, type(num_float))
num_str = str(num_float)
print(num_str, type(num_str))
num_int = int(float(num_str))
print(num_int, type(num_int))


print("question 7")
# Without breaking the expression into many lines, evaluate:
# result = "10" + str(5 * 2) + str(int("3.0"))
result = "10" + str(5 * 2) + str(int(float("3.0")))
# Tasks:
# Print the value of result
# Print the data type of result
# Explain in one sentence why the expression works

# answer
print(result)
print(type(result))
"The expression works because all components are converted to strings before concatenation, allowing them to be combined without type errors."