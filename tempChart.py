def whileLoop():
    print("Celsius","Fahrenheit")
    a=0
    while a<=100:
        celsius=a
        fahrenheit=((celsius*9/5) + 32)
        print(celsius,"         ", fahrenheit)
        a=a+5
whileLoop()

def forLoop():
    print("Celsius","Fahrenheit")
    a=0
    for a in range(0,100,5):
        celsius=a
        fahrenheit=((celsius*9/5) + 32)
        print(celsius,"      ",fahrenheit)
forLoop()
