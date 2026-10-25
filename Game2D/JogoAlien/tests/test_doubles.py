from tests.doubles import StubSemDesconto
from src.coisa_de_desconto.Desconto import Pedido

def test_pedido_com_stub():
    pedido = Pedido(StubSemDesconto())
    assert pedido.total(100) == 100