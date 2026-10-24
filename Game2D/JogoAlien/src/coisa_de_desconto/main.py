from coisa_de_desconto.Desconto import (
    Desconto,
    DescontoNormal,
    DescontoPremium,
    DescontoVip,
    vip,
)


class pedido:
    def __init__(self, valor: float, desconto: Desconto) -> None:
        self.valor = valor
        self.desconto = desconto

    def total(self) -> float:
        return self.valor - self.desconto.calcular(self.valor)


def aplicar_desconto(desconto: Desconto, valor: float) -> float:
    return desconto.calcular(valor)


def aplicar_cupom(desconto: vip, codigo: str) -> bool:
    return desconto.aplicar_cupom(codigo)


if __name__ == "__main__":
    valor = 100.0

    desconto_normal = DescontoNormal()
    desconto_vip = DescontoVip()
    desconto_premium = DescontoPremium()

    print(f"Desconto Normal: {aplicar_desconto(desconto_normal, valor)}")
    print(f"Desconto VIP: {aplicar_desconto(desconto_vip, valor)}")
    print(f"Desconto Premium: {aplicar_desconto(desconto_premium, valor)}")

    print("Cupom VIP:", aplicar_cupom(vip(), "DESC10"))
