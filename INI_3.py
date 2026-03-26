# Rosalind_ini3
# A string s of length >== 200 letters, and four integers a, b, c, and d.
# Return: The slice of string s from indices a through b and c through d.

def string_cutter():
    s = str(input("s:"))
    print(s)
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    d = int(input("d:"))
    slice1 = s[a:b+1]
    slice2 = s[c:d+1]
    print(slice1, slice2)

string_cutter()