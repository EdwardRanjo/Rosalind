# Rosalind RNA transcriptor
# A DNA string
# Return: The transcribed RNA string

def RNA_transcriptor():
    DNA = input("Paste here your DNA sequence:")
    RNA = DNA.replace('T', 'U')
    print(RNA)
    
RNA_transcriptor()
