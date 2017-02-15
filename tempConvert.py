#ask the user to enter
#convert the temp from the F to convert
#display the temp in F & convert
#give the option to continue/exit
cont = "y"
while cont == "y":
  fahrenheit = int(input("What is the current temperature in Fahrenheit "))
  celsius = (fahrenheit - 32)/(1.8)
  print ("The current temp is %d in Fahrenheit and %d in Celsius." % (fahrenheit, celsius))
  cont = input("Continue? y/n")

'''
def temperature():
    a=True
    while(a==True):
    fahrenheit = int(input("What is the current temperature in Fahrenheit? "))
    celsius = ((fahrenheit - 32 * (5 / 9))
    print("The temperature is", fahrenheit, "in fahrenheit
'''