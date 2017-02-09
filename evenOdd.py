def evenOdd(): #あなたの犬は何歳ですか?
    number = int(input("Bangō o erabu (pick a number) "))  # ask the user for the first value
    if ((number % 2) == 0):                         #
        print("Anata no bangō wa gūsūdesu (even)")
    else:
        print("Anata no bangō wa kimyōdesu (odd)")
    #print("Anata no inu wa ningen no nenrei de ", (age * 7),"-saidesu! Sono inu no tame no atarashī torikku wa arimasen, ne?") # show the user the average
evenOdd()