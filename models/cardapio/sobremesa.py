from models.cardapio.item_cardapio import ItemCardapio

class Sobremesa (ItemCardapio):

    def __init__ (self, nome, preco, tipo, tamanho, descricao):

        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
        self._descricao = descricao

    def __str__ (self):

        return f"Sobremesa {self._nome}"

    def aplicar_desconto (self):

        self._preco -= (self._preco * 0.10)