sum_total = 0
for i in range(1, 11):
    sum_total += i
print("Sum of numbers from 1 to 10:", sum_total)



 







for i in range(1, 16):
    print(f"Square of {i} is {i**2}")






sum_squares = 0
for i in range(1, 6):
    sum_squares += i**2
print("Sum of squares from 1 to 5:", sum_squares)
















for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
















for i in range(10, 0, -1):
    print(i)














number = int(input("Enter a number: "))
sum_digits = 0
while number > 0:
    sum_digits += number % 10
    number //= 10
print("Sum of digits:", sum_digits) 











number = 10
while number > 0:
    print(number)
    number -= 1











sum_total = 0
number = 1
while number <= 100:
    sum_total += number
    number += 1
print("Sum of all integers from 1 to 100:", sum_total) 












number = 1
while number <= 10:
    print(f"Square of {number} is {number**2}")
    number += 1



























    year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")






























string = input("Enter a string: ")
if string == string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome") 















number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")














height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)
print(f"BMI: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 24.9:
    print("Category: Normal weight")
elif 25 <= bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obesity")























