usuarios = []
def cadastrar (nome, email, idade):
    for pessoa in usuarios:
        if pessoa ["email"] == email:
            return "email cadastrado" 
        if idade > 18:
            usuarios.append({"nome": nome, "email": email, "idade": idade})
            return  "Cadastrado com sucesso"
        return "Cadastro permitido apenas para maiores de 18 anos"
while True:
    print("\n Cadastro de usuário")
    nome = input("Nome de usuário ou (sair)")
    if nome  == "sair":
        break
    email = input("Digite o email:")
    idade = int(input("Digite a idade:"))
    print(cadastrar(nome, email, idade))
print ("\n Usuários cadastrados")
for i in range(1, len(usuarios)):
    print (f"{usuarios[i] ['nome']} | {usuarios[i]['email']} | {usuarios[i]['idade']anos}") 
