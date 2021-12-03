import string
def wrtalpha(filepath):
    with open(filepath, "w") as file:
        for letter in string.ascii_lowercase:
            file.write(letter + "\n")
    return file

def delalpha(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()
    with open(filepath, "w") as file:
        for line in lines:
            del line
        return file

def printalpha(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()
    for line in lines:
        print(line)
    return file
#wrtalpha("C:/Users/kopor/OneDrive/Počítač/Python/101 Exercises/alphabet.txt")

delalpha("C:/Users/kopor/OneDrive/Počítač/Python/101 Exercises/alphabet.txt")

#printalpha("C:/Users/kopor/OneDrive/Počítač/Python/101 Exercises/alphabet.txt")
