n = eval(input("Enter a four digit number:"))

first = n//1000
remaining = n%1000
second=remaining//100
remaining=n%100
third=remaining//10
remaining=remaining%10
fourth=remaining

print(first)
print(second)
print(third)
print(fourth)