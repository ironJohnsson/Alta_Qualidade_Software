from abc import ABC, abstractmethod


class Desconto(ABC):
    @abstractmethod
    def calcular(self,valor):
        pass


class DescontoNormal(Desconto):
    def calcular(self,valor):
        return (valor * 0.1)

class DescontoVip(Desconto):
    def calcular(self,valor):
        return (valor * 0.2)

class DescontoPremium(Desconto):
    def calcular(self,valor):
        return (valor * 0.3)
