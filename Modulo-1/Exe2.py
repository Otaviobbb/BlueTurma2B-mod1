
nome = input("Digite uma palavra: ").lower()
print(nome)
for p in nome:
    for letra in p:
        if letra in 'aeiou':
            print(" Essas são as vogais: ",letra)
# eu não consegui fazer com que tirassae as vogais