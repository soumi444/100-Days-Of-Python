minutes = eval(input("Enter number of minutes:"))

days = minutes//60//24
years=days//365
days=days%365

print(minutes,"minutes is approximately",years," years and",days,"days")
