def print_rangoli(size):
    firstpattern = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    inner_count = 0
    for num in range(0, 10):
        if num % 2 != 0:
            firstpattern.append(num)
            inner_count += 1
            if inner_count >= n:
                break
    second_pattern = firstpattern
    second_pattern.sort(reverse=True)
    

        
n = 3
print_rangoli(n)