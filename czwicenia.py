"""

x = 42
y = 5.2
z = "siema"
p = True

print(type(x))
print(type(y))
print(type(z))
print(type(p))
"""
"""
x = int(input("Wprowadż liczbę: "))


if x % 2 == 0:
    print("Liczba parzysta")
else:
    print("Liczba jest parzyst")

"""
"""
key = 6999

x = int(input())

if key == x:
    print("Brawo")
else:
    print("bad")


"""


x = int(input("Do ilu ma policzyć: "))

for i in range(0, x+1):
    print(i)