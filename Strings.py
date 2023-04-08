#sWAP cASE
def swap_case(s):
    sentence = []
    if len(s) in range(0,1001):
        for letter in s:
            if letter.isupper():
                sentence.append(letter.lower())
            elif letter.islower():
                sentence.append(letter.upper())
            else:
                sentence.append(letter)
    return ''.join(sentence)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#String Split and Join
def split_and_join(line):
    words = line.split()
    joinedwords = '-'.join(words)
    return joinedwords

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#What's Your Name?
def print_full_name(first, last):
    print("Hello {} {}! You just delved into python.".format(first_name, last_name))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#Mutations
def mutate_string(string, position, character):
    letterslist = [letter for letter in string]
    letterslist[position] = character
    return ''.join(letterslist)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#Find a String
def count_substring(string, sub_string):
    if len(string) in range(1, 201):
        innercount = 0
        l = len(sub_string)
        for i in range(len(string)):
            s = string[i:i+l]
            if s == sub_string:
                innercount += 1
        return innercount

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

#String Validators
if __name__ == '__main__':
    s = input()
    print(any([i.isalnum() for i in s]))
    print(any([i.isalpha() for i in s]))
    print(any([i.isdigit() for i in s]))
    print(any([i.islower() for i in s]))
    print(any([i.isupper() for i in s]))





    