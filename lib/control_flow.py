#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
result = admin_login("admin", "12345")
print(result)

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
temp = hows_the_weather(86)
print(temp)

def fizzbuzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
number = fizzbuzz(35)
print(number)
    

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:  # Avoid division by zero
            return num1 / num2
        else:
            print("Error: Division by zero!")
            return None
    else:
        print("Invalid operation!")
        return None
calculation = calculator("/", 4, 0)
print(calculation)
    
    
