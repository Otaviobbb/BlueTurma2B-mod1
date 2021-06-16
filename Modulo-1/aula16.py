class aluno():
    def __init__(self, nome, idade, serie, nota1, nota2, matricula, sala):
        self.nome = nome
        self.idade = idade
        self.serie = serie
        self.nota1 = nota1
        self.nota2 = nota2
        self.matricula = matricula
        self.sala = sala
        self.media = 0

    def calcula_media(self, nota1, nota2):
        self.media =(self.nota1 + self.nota2)/2
        print(f"A media do {self.nome} é {self.media}: ")

    def altera_sala(self):
        nova_sala = input("Digite a nova sala: ") 
        confirmacao = input(f"Você quer alterar o aluno {self.nome} da sala {self.sala} para a nova sala?")
        if confirmacao == "Sim":
            self.sala = nova_sala
        else:
            print("Ok, nada alterado")
        print(f"A sala do aluno {self.nome} é: {self.sala}")  


aluno_otavio = aluno("Otavio",22,"3ano",10,2,"12345","Sala 2B")
print(aluno_otavio.nome)
print(vars(aluno_otavio))
aluno_otavio.calcula_media() 
aluno_otavio.altera_sala()
