
def appendFile(filename, text):
    with open(filename, "a") as file:
        file.write(text + "\n")

def disContent(filename):
    with open(filename, "r") as file:
        content = file.readlines()
        for line in content:
            print(line, end="") 

    return len(content)  

filename = "demo.txt"

appendFile(filename, "I am a calicut university student.")
appendFile(filename, "This is the second line.")
appendFile(filename, "This is third line of these code!")


print("\nContent of the file:")
line_count = disContent(filename)
print(f"\n\nTotal number of lines in the file: {line_count}")
