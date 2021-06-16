# a. Crie uma classe chamada bombaCombustível, com no mínimo esses atributos:
# i. tipoCombustivel.
# ii. valorLitro.
# iii. quantidadeCombustivel.
# b. A classe deve possuir no mínimo esses métodos:
# i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que
# foi colocada no veículo.
# ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor
# a ser pago pelo cliente.
# iii. alterarValor( ) – altera o valor do litro do combustível.
# iv. alterarCombustivel( ) – altera o tipo do combustível.
# v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba



class BombaCombustivel:
    def __init__ (self):
        if self.tipoCombustivel == "GASOLINA":
            self.valorLitro = 5
        else:
            self.valorLitro = 4
        self.quantidadeBombaG = 3000
        self.quantidadeBombaA = 3000 
        self.quantidadeCombustivel = 0


    def tipo(self,):
        self.tipoCombustivel = input("Vai abastecer com Álcool ou Gasolina?: ").upper()

    def abastecerPorValor(self):
        self.quantidadeCombustivel = float(input("Quanto vai abastecer campeão?: ")).replace(",",".")
        self.quantidadeCombustivel / self.valorLitro
        print(f"A quantidade de Litros foi de: {self.quantidadeCombustivel}")
        if self.quantidadeCombustivel == self.tipoCombustivel:
            self.quantidadeCombustivel - self.quantidadeBombaG
        else:
            self.quantidadeCombustivel - self.quantidadeBombaA

        
    # ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor
# a ser pago pelo cliente.
    def abastecerPorLitro(self):
        print(f"A quantidade de Litros é: {self.quantidadeCombustivel}")
        print("O valor deu : ",self.valorLitro * self.quantidadeCombustivel)

cliente = BombaCombustivel()
cliente.abastecerPorValor()

