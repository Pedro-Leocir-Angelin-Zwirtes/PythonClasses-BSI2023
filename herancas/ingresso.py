class Ingresso():
	"""Classe ingresso"""

	__slots__ = ["__valor"]

	def __init__(self, valor : float):
		"""Classe construtora"""
		
		self.valor = valor

	@property
	def valor(self):
		return self.__valor
	
	@valor.setter
	def valor(self, valor : float):

		if isinstance(valor, float):
			self.__valor = valor
		else:
			return TypeError("O valor deve ser do tipo float")

	def __str__(self):
		return f"Valor do ingresso normal : {self.valor}"
