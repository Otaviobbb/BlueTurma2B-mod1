# Essa parte pede ao usuário dois números;
n1 = float(input("Digite um número: ").replace(",","."))
n2 = float(input("Digite outro número: ").replace(",","."))
res1 = n1 + n2 
res2 = n1 * n2
res3 = (n1 // n2)

# Essa parte mostra a Soma;
print("O resultado da soma é: ",res1)
print()

# Essa parte mostra a Multiplicação;
print("O resultado da multiplicação é:  ",res2)
print()

# Essa parte mostra a Divisão;
print("O resultado da divisão inteira é: ",res3)
print()

# Essa parte mostrará qual é o maior;
if res1 > res2 and res1 > res3:
    print("Esse é o maior entre eles: ",res1)
elif res2 > res1 and res2 > res3:
    print("Esse é o maior entre eles: ",res2)
elif res3 > res1 and res3 > res2:
    print("Esse é o maior entre eles: ",res3)
else:
    print("")

# Verifica se a soma é par ou impar;
if res1 % 2 == 0:
    print("O resultado da soma é par")
else:
    print("O resultado da soma é impar")

# Verifica se a multiplicação é maior que 40 e divide pelo resultado da divisão inteira;
if res2 >= 40:
    res_final = res2 // res3
    print("O resultado da multiplicação divida pelo o resultado da divisão: ",res_final)
else:
    print("O resultado não foi maior que 40!")



