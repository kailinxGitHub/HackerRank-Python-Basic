def split_and_join(line):
    words = line.split()
    joinedwords = '-'.join(words)
    return joinedwords


line = "this is a string"
result = split_and_join(line)
print(result)