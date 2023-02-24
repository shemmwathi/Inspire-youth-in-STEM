#using for loop draw a diamond 
#Using for loop draw a trinagle
#Using forloop draw pascals triangle
 

# Get the number of rows for the diamond
# Get the size of the diamond from the user
n = int(input("Enter the size of the diamond: "))
for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(" ", end="")
    for k in range(1, 2*i):
        print("*", end="")
    print()

# Second half of the diamond
for i in range(n-1, 0, -1):
    for j in range(1, n-i+1):
        print(" ", end="")
    # Print asterisks
    for k in range(1, 2*i):
        print("*", end="")
    print()


# Get the maximum width of the hill
max_width = int(input("Enter the maximum width of the hill: "))

for i in range(1, max_width+1):
    print("*" * i)

for i in range(max_width-1, 0, -1):
    print("*" * i)






