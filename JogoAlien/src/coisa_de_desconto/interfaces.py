class IDesconto:
    def calcular(self, valor):
        raise NotImplementedError

class ICupom:
    def aplicar_cupom(self, codigo):
        raise NotImplementedError

class IUsuario:
    def validar_usuario_vip(self, usuario):
        raise NotImplementedError