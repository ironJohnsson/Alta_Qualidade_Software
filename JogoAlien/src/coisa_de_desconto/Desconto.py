from abc import ABC, abstractmethod

from interfaces import *


class Desconto(ABC):
    @abstractmethod
    def calcular(self,valor):
        pass


class DescontoNormal(IDesconto):
    def calcular(self,valor):
        return (valor * 0.1)

class DescontoVip(IDesconto):

    def calcular(self,valor):
        return (valor * 0.2)
    

class DescontoPremium(IDesconto):
    def calcular(self,valor):
        return (valor * 0.3)

class vip(IDesconto,ICupom,IUsuario):
    def calcular(self,valor):
        return (valor * 0.2)

    def aplicar_cupom(self,codigo):
        return True

    def validar_usuario_vip(self,usuario):
        return usuario=="vip"
