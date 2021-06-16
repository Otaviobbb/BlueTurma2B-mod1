class pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    def dados(self):
        print(f"O nome é : {self.nome} e o sobrenome é: {self.sobrenome} e a idade é: {self.idade}")
    
alguem = pessoa("Otavio","Matheus",22)
print(vars(alguem))
alguem.dados()