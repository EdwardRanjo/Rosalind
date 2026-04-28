# Rosalind REVP

with open("rosalind_revp.txt", "r") as f:
    s = f.read().splitlines()

dna = "".join(line for line in s if not line.startswith(">"))

def revcomp(seq):
    return seq[::-1].translate(str.maketrans("ACGT", "TGCA"))

for i in range(len(dna)):
    for length in range(4, 12 + 1):
        fragment = dna[i:i+length]

        if len(fragment) == length and fragment == revcomp(fragment):
            print(i + 1, length)