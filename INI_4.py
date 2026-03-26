# Rosalind_ini4
# Two positive integers a and b (a < b < 10000)
# Return: The sum of all odd integers from a through b inclusively

def addodd():
    a = int(input("a:"))
    b = int(input("b:"))
    odd_numbers = []
    number_list = list(range(a,b+1))
    for i in number_list:
        if i%2 == 1:
            odd_numbers.append(i)
        else: pass
    print(sum(odd_numbers))

addodd()
    