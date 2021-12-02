def Countwords(filepath):
    with open(filepath, "r") as file:
        StrgFile=file.read()
        StrgFile=StrgFile.replace(","," ")
        strgList=StrgFile.split(" ")
        return len(strgList)

print(Countwords("C:/Users/kopor/OneDrive/Počítač/Python/101 Exercises/words2.txt"))
