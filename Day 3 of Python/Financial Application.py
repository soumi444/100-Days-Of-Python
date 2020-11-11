subtotal = eval(input("what is your subtotal?"))
gratuityRate = eval(input("Enter Gratuity Rate:"))

gratuity = gratuityRate/10
total = subtotal+gratuity

print("Total is", int(total) , "gratuity is", int(gratuity))