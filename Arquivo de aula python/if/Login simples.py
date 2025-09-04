usuario = str(input("Digite o nome do usuario: "))
senha   = int(input("Digite a senha: "))

pessoa = {
    usuario,
    senha
}

if ("admin"  in pessoa ) and ( 1234 in pessoa  ):
    print("Acesso concedido ")
else :
    print("Acesso negado")
