# 1. Crie um programa onde você cadastre a data de nascimento (dd/mm/aa) de algumas
# celebridades em um dicionário. Ao escolher uma celebridade, seu programa deve
# retornar a data completa. Não esqueça de validar se a celebridade escolhida está
# presente em seu dicionário.

# Exercicio 1 (Dicionario.get(chave)) retorna o valor da chave 
# Dicionairo[chave] retorna o valor;


celebridade = {"Neymar":"1994","Messi":"1989", "Cris":"1985","Ronaldo":"1971"}
print("Já sabemos as datas de cada celebridade: ")
for name in celebridade:
    print(name)
nome = (input("Digite o nome: ")).title()
print(2021 - int(celebridade[nome]))
print(celebridade.get(nome,f"Desculnpe, o {nome} não foi encontrado !"))