# Python Code For Simple Calculator
# It only works for "addition" , "multiplication" , "subtraction" and "division".

a = float(input("enter the first number: "))

o = input("enter the operator: ")

b = float(input("enter the second number: "))

if (o=="+"):

    print(a+b)

elif (o=="-"):

    print(a-b)

elif(o=="*"):

    print(a*b)

elif(o=="/"):

    print(a/b)
else:

    print("you entered a wrong operator")
