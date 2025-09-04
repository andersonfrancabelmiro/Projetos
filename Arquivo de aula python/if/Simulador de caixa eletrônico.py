saque  = int(input("Digite o vaor para sacar: "))
saldo = saque //100
print(f"nota de 100 qtd: {saldo} ")
restsaldo = saque%100 
restsaldo = restsaldo//50
print(f"notas de  50  qtd:{restsaldo}")
restsaldo = saque%50 
restsaldo = restsaldo//20
print(f"notas de  20  qtd:{restsaldo}")
restsaldo = saque%20 
restsaldo = restsaldo//10
print(f"notas de  10  qtd:{restsaldo}")
restsaldo = saque%10 
restsaldo = restsaldo//5
print(f"notas de  5  qtd:{restsaldo}")
restsaldo = saque%5 
restsaldo = restsaldo//2
print(f"notas de  2  qtd:{restsaldo}")

