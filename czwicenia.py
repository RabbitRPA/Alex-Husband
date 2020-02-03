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
"""

x = int(input("Do ilu ma policzyć: "))

for i in range(0, x+1):
    print(i)

"""

x = 0

while x <= 5:
    print(x)
    x+=1



szukana_liczba = 40
x = 0
print("Zgadnij liczbę \nLiczba jest z zakresu 0 - 100")
while x != szukana_liczba:
    
    x = int(input("Podaj liczbę: "))
    if x == szukana_liczba:
        print("Gratulacje Zgadłeś.")
        break
    elif x > szukana_liczba:
        print("Za dużo")
    elif x < szukana_liczba:
        print("Za mało")