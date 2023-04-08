def print_formatted(number):
    if n in range(1, 100):
        for i in range(1,n+1):
            innerlist = [i, oct(i)[2:], hex(i).upper()[2:], bin(i)[2:]]
            print("  ".join(map(str, innerlist)))
        


n = 2
print_formatted(n)