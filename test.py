def add():
    n = int(input())
    myset = set()
    if n in range(0, 1000):
        for i in range(n):
            myset.add(str(input()))
    print(len(myset))

add()