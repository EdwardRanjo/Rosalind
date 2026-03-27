# Rosalind DNA Nucleotide Counter
# A string containing a DNA sequence
# Return: Four integers separated by spaces denoting the number of 'A', 'C', 'G', and 'T' bases.

def nucleotide_counter():
    DNA = input("Paste here your DNA sequence:")
    a = DNA.count('A')
    c = DNA.count('C')
    g = DNA.count('G')
    t = DNA.count('T')
    
    print(a, c, g, t)

nucleotide_counter()
       