# Rosalind_ini5
# A file containing at most 1000 lines
# Return: A file containing all the even-numbered lines from the original file.

def line_counter():
    filename = input("What is the file name of the text?:")
    with open(filename) as f:
        lines = f.readlines()
        
    for i in range(1, len(lines), 2):
        print(lines[i], end="")

line_counter()