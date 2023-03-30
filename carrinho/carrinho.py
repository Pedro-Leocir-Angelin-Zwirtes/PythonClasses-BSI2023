"""Dia 1: Crie uma classe "Carrinho" que tenha uma lista de produtos e métodos para adicionar produtos ao carrinho, 
calcular o total da compra e imprimir a lista de produtos com os seus preços."""

class Carrinho():
    """Classe construtora do carrinho de compras"""

    compras = {}

    def __init__(self, produtos:str, valor:float):
        
        if not isinstance(produtos, str):
            raise TypeError("O produto deve ser uma string")
    
        if not isinstance(valor, float):
            raise TypeError("O valor deve ser do tipo real - float")
        
        try:

            self.produtos = produtos
            self.valor = valor

        except Exception as e:
            raise e

    def adicionar_produtos(self):
        """Método responsável por adicionar os produtos ao carrinho"""

        self.compras[self.produtos] = self.valor 
        print(self.compras)


    def calcular_carrinho(self) -> float:
        """Método responável por calcular o total dos produtos no carrinho"""

        soma = self.compras.values()
        return f"O valor total do carrinho é de: {self.soma}"

    def __str__(self):
        """Método que retorna um texto a ser apresentado para o usuário"""

        return f"produto={self.produtos}, valor={self.valor} Compra efetuada!"