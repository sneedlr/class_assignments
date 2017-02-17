print("Sentaur has been summoned")
def main():
    a = input("Enter yes to continue or no to exit:  ")
    if a=="yes" or "y" :
            import tkinter as tk
            from tkinter import filedialog
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename()
    elif a=="no":
            print("Goodbye")
    numLines = 0
    numWords = 0
    numChars = 0

    with open(file_path,"r")as file:
        for line in file:
            wordsList = line.split()
            numLines += 1
            numWords += len(wordsList)
            numChars += len(line)
    print (numLines,"lines", numWords,"words &", numChars, "characters")
main()
'''total word count
avg words per sentence'''