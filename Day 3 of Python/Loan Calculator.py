loanAmount = eval(input("What is your loan amount?"))
annualInterestRate = eval(input("What is the interest Rate on your loan amount?"))
numberOfYears = eval(input("Number Of Years?"))

monthlyInterestRate = annualInterestRate/1200

monthlyPayment = loanAmount * monthlyInterestRate/ (1-1/(1+monthlyInterestRate)**numberOfYears)
totalPayment = monthlyPayment*numberOfYears*12

print("The monthly Payment is :", int(monthlyPayment))
print("The total Payment is :", int(totalPayment))