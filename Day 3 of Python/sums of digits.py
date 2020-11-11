number = eval(input("Enter a number between 0 and 1000:"))

number1 = number//100
remaining = number%100
number2 = remaining//10
remaining=number%10
number3 = remaining

total = int(number1 + number2 + number3)

print("Total is",int(total))