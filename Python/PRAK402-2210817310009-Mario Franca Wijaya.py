angka = int(input())
for i in range(1, angka):
    if i % 2 != 0 :
        print(i, end = ' ')
print('\n')
while angka > 0:
    if angka % 2 == 0:
        print(angka, end = ' ')
    angka -= 1
