#create a table
from prettytable import PrettyTable
columns =[" Name","Roll number","Residence"]
mytable = PrettyTable()

mytable.add_column(columns[0],["Priscilla Waimani","Pooh shiesty","Ben Afflex","Clark Kent", ] )

mytable.add_column(columns[1],[1 ,2 ,3 ,4])

mytable.add_column(columns[2],["City hall","Memphis","Gotham City","Metropolis"])

print(mytable)

                   
