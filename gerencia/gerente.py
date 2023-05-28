from empregado import Empregado

class Gerente(Empregado):
    """Classe para o departamento do gerente?"""

    __slots__ = ["__departamento"]

    def __init__(self, nome : str, departamento : str):
        """Classe construtora"""

        super().__init__(nome)

        self.departamento = departamento

    @property
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self, departamento : str):

        if not hasattr(self, "__departamento"):
             self.__departamento = None

        if isinstance(departamento, str) and departamento != self.__departamento:
                self.__departamento = departamento
        else:
            return ValueError("O departamento deve ser do tipo str")
        
    def __str__(self):
         return f"O nome do empregado é : {super().nome}\nO departamento é : {self.__departamento}"
