#calculator Program V.1
#Programmer: Dena, Rene

print ('\n\nWelcome to "Calculate my Numbers!"')

name = input ("\nHello, what's your name?")

print ("\nHi there,",name)

X = int(input("\nPlease enter your first number:"))
Y = int(input("Please enter your second number:"))

print ("\nHere are the mathematical operations of witch will be utilized.")

print ("\nA = Addition")
print ("B = Subtraction")
print ("C = Multiplication")
print ("D = Division w/ decimal")
print ("E = Division w/o decimal")
print ("F = Remainder")
print ("G = Equality") #fix this product
print ("H = Diffrence")
print ("I = Exponent")
print ("J = Less than")
print ("K = Less than or equal too")
print ("L = Greater than")
print ("M = Greater than or equal too")

A = X+Y
B = X-Y
C = X*Y
D = X/Y
E = X//Y
F = X%Y
G = X==Y
H = X!=Y
I = X**Y
J = X<Y
K = X<=Y
L = X>Y
M = X>=Y


print ("\nHere are the solutions for each operations listed above:")
print("\n")

if A :
    print ("A:", X, 'plus', Y, "equals;", '"',A,'"')
if B :
    print ("B:", X, 'minus', Y, "equals;", '"',B,'"')
if C :
    print ("C:", X, 'times', Y, "equals;", '"',C,'"')
if D :
    print ("D:", X, 'divided by', Y, "gives you a decimal of;", '"',D,'"')
if E :
    print ("E:", X, 'divided by', Y, "gives you a whole number of;", '"',E,'"')
if F :
    print ("F:", X, 'divided by', Y, "gives you a remainder of;", '"',F,'"')
if G :
    print ("G:", "is", X, 'equal too', Y, "results in;", '"',G,'"')
if H :
    print ("H:", X, 'is not equal to', Y, "results in;", '"',H,'"')
if I :
    print ("I:", X, '**', Y, "-", '"',I,'"')
if J :
    print ("J:", X, 'is less than', Y, "results in;", '"',J,'"')
if K :
    print ("K:", X, 'is less than OR equal too', Y, "results in;", '"',K,'"')
if L :
    print ("L:", X, 'is greater than', Y, "results in;", '"',L,'"')
if M :
    print ("M:", X, 'is greater than OR equal too', Y, "results in;", '"',M,'"')

    
input("\n\nPress the ENTER key to exit.")


