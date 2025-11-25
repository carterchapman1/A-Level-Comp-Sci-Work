"""number = int(input('Pick a number 0-99 \n'))
mode = input("Multiplicative or additive persitence (a or m) \n")
count = 0
while number > 9:
    if mode == 'a':
        number = ((number // 10) + (number % 10))
    elif mode == 'm':
        number = ((number // 10) * (number % 10))
    count +=1
print(f"The Persitance = {count}, {number}")"""
    

number1 = int(input("enter a whole number "))
number2 = int(input("enter another whole number "))
temp1 = number1
temp2 = number2

while temp1 != temp2:
    if temp1 > temp2:
        temp1 -= temp2
    else:
        temp2 -= temp1

print(f"{temp1} is the GCF of {number1} and {number2}")