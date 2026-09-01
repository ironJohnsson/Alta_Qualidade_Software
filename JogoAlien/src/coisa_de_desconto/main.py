from Desconto import DescontoNormal, DescontoPremium, DescontoVip


def main():
    valor = float(input("Digite o valor da compra: "))
    tipo = input("Digite o tipo de cliente (normal, vip, premium): ").strip().lower()

    if tipo == "normal":
        desconto = DescontoNormal()
    elif tipo == "vip":
        desconto = DescontoVip()
    elif tipo == "premium":
        desconto = DescontoPremium()
    else:
        print("Tipo de cliente inválido.")
        return

    valor_final = desconto.calcular(valor)
    print(f"Valor final: R$ {valor_final:.2f}")


if __name__ == "__main__":
    main()