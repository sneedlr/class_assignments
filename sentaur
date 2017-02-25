print("Sentaur has been summoned")
print("Lets get started")

from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()

def main():
    try:
        numWords = 0
        numSents = 0
        count=0
        a = input("Enter 'Yes' to continue or 'No' to exit ")
        if a.lower()=="yes":
            f=askopenfilename()
            with open(f,"r")as file:
                for line in file:
                    numSents += line.count('.') + line.count('!') + line.count('?')
                    wordsList = line.split()
                    numWords += len(wordsList)

                for i in range(len(wordsList)):
                    k=wordsList[i]
                    if 3<= len(k) <=8:
                        count += 1
                    i+=1
            print ("Total # of words: ", count,"Average words per sentence is: ", count / numSents,"wps")
        elif a.lower() == "no":
            print("Goodbye")
        elif a.lower() != "yes" or "no":
            print("Please enter Yes or No")
            main()
    except:
        main()
main()
