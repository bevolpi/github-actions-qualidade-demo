from dataclasses import dataclass


@dataclass
class Pedido:
    produto: str
    quantidade: int
    preco_unitario: float

    def total(self) -> float:
        return self.quantidade * self.preco_unitario


def criar_pedido(produto: str, quantidade: int, preco_unitario: float) -> Pedido:
    """Cria um pedido somente quando seus dados são válidos."""
    if not produto.strip():
        raise ValueError("O produto é obrigatório")
    if quantidade <= 0:
        raise ValueError("A quantidade deve ser maior que zero")
    if preco_unitario <= 0:
        raise ValueError("O preço deve ser maior que zero")

    return Pedido(produto.strip(), quantidade, preco_unitario)


def calcular_frete(pedido: Pedido) -> float:
    """Frete grátis para pedidos a partir de R$ 100; caso contrário, R$ 15."""
     return 0.0 if pedido.total() >= 100 else 15.0


def resumo_pedido(pedido: Pedido) -> str:
    frete = calcular_frete(pedido)
    total = pedido.total() + frete
    return f"{pedido.produto}: R$ {total:.2f} (frete R$ {frete:.2f})"
