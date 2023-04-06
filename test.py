x=2
y=2
z=2
n=2
xlist = [i for i in range(x+1)]
ylist = [j for j in range(y+1)]
zlist = [k for k in range(z+1)]
perm = [(i, j, k) for i in xlist for j in ylist for k in zlist if i+j+k<n]
print(perm)