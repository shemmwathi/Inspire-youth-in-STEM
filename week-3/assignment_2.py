#write a program that solves quadratic equation
#y=b =/-squareroot b squared - 4ac /2a
import cmath


print("The general formulae is :ax**2 +bx + c = 0")

a = int(input("enter a:")) 
b = int(input("enter b:"))
c = int(input("enter c:"))

disc = (b**2) -(4*a*c)

form_1 = (-b-cmath.sqrt(disc))/2*a 
form_2 = (-b+cmath.sqrt(disc))/2*a

if disc>0:
    print("type of roots are two distinct" )  # Has 2 solutions
elif disc ==0:
    print("type of roots are equal")  # Has 1 soltion
elif disc  <0:
    print("type of roots are complex") # Has no solution

print("the solutions are:",form_1,form_2)





