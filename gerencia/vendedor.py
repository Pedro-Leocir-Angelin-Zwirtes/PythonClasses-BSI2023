from empregado import Empregado

class Vendedor(Empregado):
    """Classe para a comissão do vendedor"""

    __slots__ = ["__percentualComissao"]

    def __init__(self, nome : str, percentualComissao : float):
        """Classe construtora"""

        super().__init__(nome)

        self.percentualComissao = percentualComissao

    @property
    def percentualComissao(self):
        return self.__percentualComissao
    
    @percentualComissao.setter
    def percentualComissao(self, percentualComissao : float):

        if not hasattr(self, "__percentualComissao"):
             self.__percentualComissao = None

        if isinstance(percentualComissao, float) and percentualComissao != self.__percentualComissao:
                self.__percentualComissao = percentualComissao
        else:
            return ValueError("O nome deve ser do tipo str")
        
    def __str__(self):
         return f"O nome do empregado é : {super().nome}\nA comissão é : {self.__percentualComissao}%"
