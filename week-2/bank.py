#write a program that calculates 16% tax on income
#ranging between 100,000 - 150,000

#19% tax on income  that is between 150,000-300,000

#30% tax income is above 300,000

#5% tax income is less than 100,000

#print gross income, net income

gross_income = int(input("Enter your gross income :"))

taxgroup_1 =(gross_income * 0.15)
taxgroup_2 =(gross_income * 0.16)
taxgroup_3 =(gross_income * 0.19)
taxgropu_4 =(gross_income * 0.30)

if gross_income <= 100000:
    print("gross_income",gross_income)
    print("tax:",taxgroup_1)
    print("net_income:",gross_income - taxgroup_1)

elif (gross_income(int>=100001)) & (gross_income< 150,000):
    print("gross_income:",gross_income)
    print("tax:",taxgroup_2)
    print("net_income:",gross_income - taxgroup_2)

elif (gross_income>=150001) & (gross_income<=300000):
    print("gross_income:",gross_income)
    print("tax:",taxgroup_3)
    print("net_income:",gross_income - taxgroup_3)

elif (gross_income>=300001):
    print("gross_income:",gross_income)
    print("tax:",taxgropu_4)
    print("net_income:", gross_income - taxgropu_4)
    
