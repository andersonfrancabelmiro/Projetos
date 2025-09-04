print('===============Operações matemáticas===============')

PriNum = int(input('Digite um numero: '))
SegNum = int(input('digite outro numero: '))

soma = PriNum + SegNum
sub  = PriNum - SegNum
mult = PriNum * SegNum
divi = PriNum / SegNum

print('{} + {} = {}'.format(PriNum,SegNum,soma))
print('{} - {} = {}'.format(PriNum,SegNum,sub))
print('{} * {} = {}'.format(PriNum,SegNum,mult))
print('{} / {} = {}'.format(PriNum,SegNum,divi))