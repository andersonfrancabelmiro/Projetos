PriNum = int(input('Digite um numero:'))
SegNum = int(input('Digite outro numero:'))

if PriNum > SegNum:
    print(f'O {PriNum} maior que {SegNum}')
elif PriNum < SegNum:
    print(f'O {PriNum} menor que {SegNum}')
else :
    print('Os numero sao iguais')
