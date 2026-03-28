# Rosalind GC Content
# DNA strings in FASTA format
# Return: The ID of the DNA string with the highest GC Content followed by the GC Content of that string.

def gc_count():
    filename = input("What is your FASTA file?:")
    with open(filename) as f:
        sequences = {}
        current_header = None
        
        for line in f:
            line = line.strip()
            
            if line.startswith(">"):
                current_header = line[1:]
                sequences[current_header] = ""
            else: sequences[current_header] += line

    max_gc = 0
    max_id = ""
    
    for header, seq in sequences.items():
        gc = seq.count('G') + seq.count('C')
        total = len(seq)
        gc_content = (gc / total) * 100
 
    if gc_content > max_gc:
        max_gc = gc_content
        max_id = header
    
    
    print(max_id)
    print(max_gc)

gc_count()