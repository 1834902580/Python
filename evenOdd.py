
def even(num):
    if num % 2 == 0:
        return True
    else:
        return False
arr=[]
arr2=[]
starting = 1
user=int(input('number: '))
# while starting <= user:
#     if even(starting):
#         arr.append(starting)
#         print(f'{starting} is even:')
#     else:
#         print(f'{starting} is odd')
#         arr2.append(starting)
#     starting=starting+100

for num in range(0,user+1):
    if even(num):
        arr.append(num)
        print(f'{num} is even:')
    else:
        print(f'{num} is odd :')
        arr2.append(num)
    num=num+1

print(f'even numbers {arr}')
print(f'odd numbers {arr2}')