from ingresso import Ingresso

class IngressoVip(Ingresso):
	"""Classe para criação do ingresso vip"""

	__slots__ = ["__valorAdicional"]

	def __init__(self, valor: float, valorAdicional : float):
		"""Classe construtora"""

		super().__init__(valor)

		self.valorAdicional = valorAdicional

	@property
	def valorAdicional(self):
		return self.__valorAdicional
	
	@valorAdicional.setter
	def valorAdicional(self, valorAdicional : float):

		if isinstance(valorAdicional, float):
			self.__valorAdicional = valorAdicional
		else:
			return TypeError("O valorAdicional deve ser do tipo float")


	def __str__(self):
		valorTotal = self.valor + self.__valorAdicional
		return "Valor do ingresso VIP : {:.2f}".format(valorTotal)
