num = int(input('Your marks '))
print(num)


def tarif(x):
    print(f"You got: {x}")

if num >= 80 and num <= 100:
    tarif('A+')

elif num >= 70 and num < 80:
    tarif('A')

elif num >= 60 and num < 70:
    tarif('A-')

elif num >= 50 and num < 60:
    tarif('B')
elif num >= 40 and num < 50:
    tarif('C')
elif num >= 33 and num < 40:
    tarif('D')
else:
    tarif('F')
