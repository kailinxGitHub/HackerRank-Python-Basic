def count_substring(string, sub_string):
    innercount = 0
    sunique = set()
    newstring = [i for i in string if i not in sunique and not sunique.add(i)]
    ssunique = set()
    newsub_string = [j for j in sub_string if j not in ssunique and not ssunique.add(j)]
    for k in newstring:
        for z in newsub_string:
            if k == z:
                innercount += 1
    return innercount

string = "ABCDCDC".strip()
sub_string = "CDC".strip()
count = count_substring(string, sub_string)
print(count)