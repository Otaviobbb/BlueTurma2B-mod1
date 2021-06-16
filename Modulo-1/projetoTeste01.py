# Proposta de projeto de ficção interativa para avaliação de OO
# Sugestão: completar com classes filhas colocando pessoas saudáveis, 
# trabalhos menos remunerados, casas melhor equipadas et cetera



# Classe para a criação do objeto tipo relógio para iteração de tempo no programa;
class Relogio:
    def __init__(self): # Construtor padrão com dois atributos assumidos;
        self.horas = 7
        self.minutos = 0
    
    def __str__(self): # Método para retornar mensagem;
        return f"{self.horas:02d}:{self.minutos:02d}"
    
    def avancaTempo(self, minutos):  # Método para validar minutos em horas e alterar os contadores de minutos e de horas;
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1
    
    def atrasado(self): # Método para definir o ponto (tempo) para o inicio do atraso;
        return (self.horas > 8 or (self.horas == 8 and self.minutos > 0))

# Teste de alterações;
tempo = Relogio()
tempo.avancaTempo(60)
tempo.atrasado()
print(vars(tempo))

# classe paar criação do personagem;
class Personagem:
    def __init__(self,nome):
        self.nome = nome 
        self.nivel = "Junior"
        self.sujo = True
        self.fome = True
        self.medicado = False
        self.dinheiro = 0
        self.salario = 100
    def __str__(self):
        return f"Olá {self.nome} Você é um Programador {self.nivel} e acaba de ingressar á equipe Blue Edtech. Você está " + ("sujo" if self.sujo else "limpo")+", "+("com" if self.fome else "sem")+" fome e "+("" if self.medicado else "não ")+"tomou sua medicação. Você tem "+str(self.dinheiro)+" reais na sua conta."

    def dormir(self):
        self.sujo = True
        self.fome = True
        self.medicado = False

# Teste de alterações;
programador = Personagem("Janio")
programador.dormir()
print(vars(programador))

# Classe para armazenar quantidade de alimentos na dispensa da casa;
class Dispensa:
    def __init__(self, remedios, cafe, almoco, jantar):
        self.remedios = remedios
        self.cafe = cafe
        self.almoco = almoco
        self.jantar = jantar

# Teste de alterações;
refeicoes = Dispensa(1, 1, 1, 1)
