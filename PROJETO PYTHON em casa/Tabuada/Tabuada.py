numero = int(input('Digite um numero: '))

for i in range(1,11):
    tabu = numero * i
    print(f'{numero} x {i} = {tabu} ')


print('=========================================')

a = 1
while a <= numero:
    tabua = numero *  a
    print(f'{numero} x {a} = {tabua} ')
    a += 1