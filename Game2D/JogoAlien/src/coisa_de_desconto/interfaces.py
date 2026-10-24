class IDesconto:
    def calcular(self, valor: float) -> float:
        raise NotImplementedError


class ICupom:
    def aplicar_cupom(self, codigo: str) -> bool:
        raise NotImplementedError


class IUsuario:
    def validar_usuario_vip(self, usuario: str) -> bool:
        raise NotImplementedError
