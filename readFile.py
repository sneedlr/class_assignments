file= open("test.txt", "r") #opens file with name of "test.txt"
myList = []
for line in file:
    myList.append(line)
    print(myList)