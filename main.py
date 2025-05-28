#task-1-Hello Variable World
greetings = "Hello, Python World!"
print(greetings)



#task-2-Basic Math Operations
x = int(input('Input first number: '))
y = int(input('Input second number: '))
addition = x+y
subtraction = x-y
multiplication = x*y
division = x/y
print(f"Our numbers are {x} and {y}, here is addition: {addition}, subtraction: {subtraction}, multiplication: {multiplication} and division: {division} of those numbers")




#task-3-String Manipulation
first_str = 'str'
second_str = 'ing'
length = len(first_str+second_str)
print(f"{first_str+second_str}, and length is {length} symbols")




#task-4-Conditional Logic
numb = int(input('Input number to check if it is odd or even: '))
if numb%2 ==0:
    print("Your number is even")
else:    
    print("Your number is odd")




#task-5-Simple Loop
for i in range (1,11):
    print(i, end = " ")




#task-6-If-Else Conditions
number = int(input())
if number > 0:
    print(f"Number {number} is positive")
elif number < 0:
    print(f"Number {number} is negative")
else:
    print(f"Number {number} is zero")




#task-7-Even Numbers with Range
for i in range(1,11):
    if i % 2 == 0:
        print(i, end = " ")




#task-8-Summing Numbers
a = int(input())
suma = 0
while i != a:   
    suma = suma + i
print(f"Sum of all numbers equals to {suma}")




#task-9-Countdown Loop
for i in range(10,0,-1):
    print(i, end = " ")




#task-10-Selective Looping
for i in range(1,11):
    if i == 5:
        continue
    elif i == 7:
        break
    print(i, end = " ")