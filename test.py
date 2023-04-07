def mutate_string(string, position, character):
    letterslist = [letter for letter in string]
    letterslist[position] = character
    return ''.join(letterslist)

s = 'abracadabra'
i, c = 5, "k"
s_new = mutate_string(s, int(i), c)
print(s_new)