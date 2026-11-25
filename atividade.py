def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self._tipo = tipoCombustivel
        self._preco = float(valorLitro)
        self._estoque = float(quantidadeCombustivel)

    @property
    def tipoCombustivel(self):
        return self._tipo

    @tipoCombustivel.setter
    def tipoCombustivel(self, nome):
        if nome:
            self._tipo = nome

    @property
    def valorLitro(self):
        return self._preco

    @valorLitro.setter
    def valorLitro(self, preco):
        if preco > 0:
            self._preco = float(preco)

    @property
    def quantidadeCombustivel(self):
        return self._estoque

    @quantidadeCombustivel.setter
    def quantidadeCombustivel(self, qtd):
        if qtd >= 0:
            self._estoque = float(qtd)

    def abastecerPorValor(self, quantia):
        if quantia <= 0:
            print("Valor invalido.")
            return
        volume = quantia / self._preco
        if volume > self._estoque:
            print("Sem combustivel suficiente na bomba.")
            return
        self._estoque -= volume
        print(f"Foram abastecidos {volume:.2f} litros.")

    def abastecerPorLitro(self, volume):
        if volume <= 0:
            print("Quantidade invalida.")
            return
        if volume > self._estoque:
            print("Sem combustivel suficiente na bomba.")
            return
        total = volume * self._preco
        self._estoque -= volume
        print(f"Total a pagar: R$ {total:.2f}")

    def __str__(self):
        return (
            f"Combustivel: {self._tipo} | "
            f"Preco/L: R$ {self._preco:.2f} | "
            f"Disponivel: {self._estoque:.2f} L"
        )

## ---------------------------------------------------------------------------- ##

#classe bomba
class BombaCombustivel():

  def __init__(self, tipo_comb, valor_litro, qtde_comb):
    self.__tipo_comb = tipo_comb
    self.__valor_litro = valor_litro
    self.__qtde_comb = qtde_comb

  def get_valor_litro(self):
    return self.__valor_litro

  def set_valor_litro(self, valor_litro):
    if valor_litro > 0:
      self.__valor_litro = valor_litro
    else:
       raise ValueError("O valor do litro deve ser maior que zero")
  #exemplo de property
  valor_litro = property(get_valor_litro,set_valor_litro)

## ---------------------------------------------------------------------------- ##

b = BombaCombustivel("alcool", 5.98, 3000)

try:
    b.valor_litro = -50
except ValueError as e:
    print(f"Erro esperado capturado: {e}")

b.valor_litro = 4.99
print(f"Novo valor do litro: R$ {b.valor_litro:.2f}")
