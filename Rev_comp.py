# Rosalind Reverse Complement
# A DNA string
# Return: The reverse complement strand of DNA string

def rev_comp():
    DNA = input("Paste here your DNA sequence:")
    rev = DNA[::-1]
    out = rev.translate(str.maketrans("ACGT", "TGCA"))
    print(out)
    
rev_comp()