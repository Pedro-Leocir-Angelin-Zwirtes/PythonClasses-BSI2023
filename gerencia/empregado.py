class Empregado():
    """Classe para a criação de um empregado"""

    __slots__ = ["__nome"]

    def __init__(self, nome : str):
        """Classe construtora"""

        self.nome = nome

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome : str):

        if not hasattr(self, "__nome"):
             self.__nome = None

        if isinstance(nome, str) and nome != self.__nome:
                self.__nome = nome
        else:
            return ValueError("O nome deve ser do tipo str")
        
    def __str__(self):
         return f"O nome do empregado é : {self.__nome}"
