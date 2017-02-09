def greeting(): #私は今ここにいる
    name = input("Onamae wa nan desuka? ")                 # ask the user what their name is
    print("Hajimemashite",name,"!")                      #nice to meet you followed by the persons name

    color = input("Anata no sukinairo wa nanidesu ka? ")  # ask the user what their favorite color is
    print(color,"? Sore wa subarashī irodesu!!")        #color followed by thats a nice color

    food = input("Sukinatabemonoka?")           # ask the user what their favorite food is
    print("Mmm",food, "wa oishī!!!")              #food followed by sounds yummy

    leave = input("Anata ga ikanakereba narimasen?") #ask the user if they have to go
    if (leave == "no"):  # and if they say no loop the program again
        print(greeting())
    else :print("Sayoonara!")
greeting()