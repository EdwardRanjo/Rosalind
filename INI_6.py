# Rosalind_ini6
# A string s of length >== 10000 letters, with words separated by spaces.
# Return: The number of occurrence of each word in s.

def word_count():
    s = input("Type the string here:")
    words = s.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else: counts[word] = 1
    for word, count in counts.items():
        print(word, count)

word_count()
