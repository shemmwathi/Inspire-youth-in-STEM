#write a program that calculates 16% tax on income
#ranging between 100,000 - 150,000

#19% tax on income  that is between 150,000-300,000

#30% tax income is above 300,000

#5% tax income is less than 100,000

#print gross income, net income

income = str(input("Enter your taxable income :"))
if income <= 100_000:
    income1 = (income ) * 0.5
elif 100_000 < income <= 150_000:
    income2= (income - 100_000)* 0.16
    print ("Your tax amount to be paid is :",income2)
elif 150_000 < income <= 300_000:
    income3 = ((income - 10_000)*0.19)
if income > 300_000:
    income4 = ((income - 300_000)*0.3)
    print ("Your tax amount to be paid is :",income)
