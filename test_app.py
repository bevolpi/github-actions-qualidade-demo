import pytest

from app import calcular_frete, criar_pedido, resumo_pedido


def test_pedido_acima_de_cem_tem_frete_gratis():
    pedido = criar_pedido("Livro", 2, 60.0)
    assert calcular_frete(pedido) == 0.0


def test_pedido_abaixo_de_cem_paga_frete():
    pedido = criar_pedido("Caneca", 1, 30.0)
    assert calcular_frete(pedido) == 15.0


def test_nao_permite_quantidade_zero():
    with pytest.raises(ValueError, match="quantidade"):
        criar_pedido("Caderno", 0, 20.0)


def test_resumo_mostra_total_e_frete():
    pedido = criar_pedido("Livro", 2, 60.0)
    assert resumo_pedido(pedido) == "Livro: R$ 120.00 (frete R$ 0.00)"
