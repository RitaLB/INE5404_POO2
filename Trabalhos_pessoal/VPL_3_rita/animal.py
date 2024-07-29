from abc import ABC, abstractmethod

class Animal(ABC):

	def __init__(self, tamanho_passo: int):
		self.__tamanho_passo = tamanho_passo

	#@property irá possibilitar consultar dado de atributo privado. 
	@property
	def tamanho_passo(self):
		pass

	# @nomeatributo.setter irá possibilitar a modificação do atributo privado.
	@tamanho_passo.setter
	def tamanho_passp(self, tamanho_passo):
		self.__tamanho_passo = tamanho_passo

	def mover(self):
		mensagem = ("ANIMAL:DESLOCOU"+ self.__tamanhoPasso)
		return mensagem
	
	@abstractmethod
	def produzir_som(self):
		pass