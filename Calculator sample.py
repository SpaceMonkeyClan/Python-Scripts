#calculator Program V.1
#Programmer: Dena, Rene

print ('\n\nWelcome to "Calculate my Numbers!"')

name = input ("\nHello, what's your name?")

print ("\nHi ",name)

X = int(input("\nPlease enter your first number:"))
Y = int(input("Please enter your second number:"))

print ("\nWhat mathematical operation would you like to utilize?")

print ("\nA = Addition")
print ("B = Subtraction")
print ("C = Multiplication")
print ("D = Division w/ decimal")
print ("E = Division w/o decimal")
print ("F = Remainder")
print ("G = Equality")
print ("or")
print ("H = Diffrence")

A = X+Y
B = X-Y
C = X*Y
D = X/Y
E = X//Y
F = X%Y
G = X==Y
H = X!=Y


print ("\nEnter the letter in capitalization in which corresponds with the operation of which you would like to execute please:")

if A :
    print ("A =", A)
if B :
    print ("B =", B)
if C :
    print ("C =", C)
if D :
    print ("D =", D)
if E :
    print ("E =", E)
if F :
    print ("F =", F)
if G :
    print ("G =", G)
if H :
    print ("H =", H)

input("\n\nPress the ENTER key to exit.")


