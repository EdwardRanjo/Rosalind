# Rosalind_ini2
# Two positive integers a and b, each less than 1000
# Return: The integer corresponding to the square of the hypotenuse of a right triangle with side lengths a and b.

def hypotenuse2(a,b):
    c = (a**2) + (b**2)
    print(c)

a = int(input("a:"))
b = int(input("b:"))

hypotenuse2(a,b)
