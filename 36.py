#DONT FORGET TO CHANGE FILE PATH BEFORE YOU RUN PROGRAM
def Countwords(filepath):
    with open(filepath, "r") as file:
        StrgFile=file.read()
        strgList=StrgFile.split(" ")
        return len(strgList)

print(Countwords("C:/Users/kopor/OneDrive/Počítač/Python/101 Exercises/words1.txt"))
