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

#Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Text Wrap
import textwrap
def wrap(string, max_width):
    outlist = []
    for i in range(0,len(string), max_width):
        for j in range(max_width+1):
            s = string[i:i+j]
            if j == max_width:
                outlist.append(s)
            else: 
                continue
    return "\n".join(outlist)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#Designer Door Mat

#String Formatting
def print_formatted(number):
    w=len(str(bin(number))[2:])
    if number in range(1, 100):
        for i in range(1,number+1):
            print(str(i).rjust(w,' '),oct(i)[2:].rjust(w,' '),hex(i)[2:].upper().rjust(w,' '),bin(i)[2:].rjust(w,' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#Alphabet Rangolo


#Capitalize!
import math
import os
import random
import re
import sys
def solve(s):
    return " ".join([x.capitalize() for x in s.split(" ")])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#The Minion Game

#Merge the Tools!

