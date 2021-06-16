from random import randint, randrange
# parte onde cadastra a senha do usario
nome = input("Digite um apelido: ").title()
senha1 = input("Cadastre uma senha: ")
print("Senha cadastrada com sucesso !!!")
senha2 = input("Para continuar, digite sua senha: ")
# aqui começa a bagunça do while
# essa parte é para verificar a senha
while senha1 != senha2:
    print("Senha incorreta, por favor tente novamente!")
    senha1 = input("Cadastre uma senha: ")
    senha2 = input("Para continuar, digite sua senha: ")
    if senha1 == senha2:
        print(f"Bem vindo(a) {nome}, ao mundo da adivinhação!")
    else:
        print()
print("VAMOS JOGAR !")
nuemro_ale = randint(0,20)
n2 = int(input("Tente advinhar o número que eu pensei de 0 a 20: "))
tentativa = 0  #aqui era para contar as tentativas de acerto

# essa parte é a verificação se acertou ou não
while n2 != nuemro_ale:
    tentativa +=1
    print("hum... Vc não acertou, Vamos tentar novamente?")
    if n2 > nuemro_ale:
        print("Acho que chutou alto, tenta novamnete!")
    if n2 < nuemro_ale:
        print("hmm... dessa vez foi um número menor! Tente de novo: ")
    print("Esse foi o número que eu tinha pensado: ",nuemro_ale)
    nuemro_ale = randrange(0,20)
    tentativa = int(input("Tente advinhar novamente o número que eu pensei de 0 a 20: "))
    if nuemro_ale == n2:
        print("UAUU !!! Vc é um gênio!!! essa foi a resposta: ", nuemro_ale,)
        print(f"Você tentou {tentativa} vezes")




    
    
