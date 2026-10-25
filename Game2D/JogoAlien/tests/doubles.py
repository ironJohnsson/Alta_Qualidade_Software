from src.coisa_de_desconto.Desconto import IDesconto

class StubSemDesconto(IDesconto):
    def calcular(self, valor):
        return 0