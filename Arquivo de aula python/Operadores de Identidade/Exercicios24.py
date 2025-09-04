PriNum = int(input('Digite um numero:'))
SegNum = int(input('Digite outro numero:'))
TerNum = int(input('Digite outro numero:'))

a = [PriNum, SegNum, TerNum ]
b = a
c = [SegNum,PriNum,TerNum]

print (a == c)
print (a is not c)
print (a is not b)



