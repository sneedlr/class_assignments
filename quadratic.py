def quadratic():
    a = int(input("Enter the value for a:"))
    b = int(input("Enter the value for b:"))
    c = int(input("Enter the value for c:"))
    x = int(input("Enter the value for x:"))
    formula = ((a*(x**2)) + (b*x) + c)
    print("The following quadratic was entered: ",a,"(",x,"^2)+ ",b,"(",x,"+4)")
    print("The value of the quadratic is ",formula)
quadratic()