class Pessoa:
    def __init__(self,nome,idade,cpf,telefone):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf 
        self.__telefone = telefone
# metodo get - para pegar, receber - defino o metodo que vai passar o valor 
    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

    def getCPF(self):
        return self.__cpf
    
    def getTelefone(self):
        return self.__telefone
# metodo set = alterar o valor de um atributo
    def setNome(self,nome):
        self.__nome = nome

    def setIdade(self,idade):
        self.__idade = idade 

    def setCPF(self,cpf):
        self.__cpf = cpf

    def setTelefone(self,telefone):
        self.__telefone = telefone 
        

pessoa = Pessoa("Otavio",22,"123142123-30","1199999999")