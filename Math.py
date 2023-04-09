#Polar Coordinates
import cmath

def polar_coordinates(z):
    print(abs(complex(z)))
    print(cmath.phase(complex(z)))

z = input()
polar_coordinates(z)

#Find Angle MBC
import math
def find_angle_mbc(line1, line2):
    if (line1 and line2) in range(0, 101):
        print(f"{round(math.degrees(math.atan(ab/bc)))}\N{DEGREE SIGN}")

ab = float(input())
bc = float(input())
find_angle_mbc(ab, bc)

#Triangle Quest 2
for i in range(1,int(input())+1): 
    print(((10**i)//9)**2)

#Mod Divmod
a = int(input())
b = int(input())

print(divmod(a,b)[0])
print(divmod(a,b)[1])
print(divmod(a,b))

#Power - Mod Power
a = int(input())
b = int(input())
m = int(input())

if (a and b) in range(1, 11) and m in range(2, 1001):
    print(pow(a,b))
    print(pow(a,b,m))

#Integers Come In All Sizes
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a and b and c and d) in range(1, 1001): 
    print(a**b+c**d)

#Triangle Quest
for i in range(1,int(input())):
    print((10**i)//9*i)
