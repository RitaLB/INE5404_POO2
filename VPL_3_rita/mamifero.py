from abc import ABC, abstractmethod
from animal import Animal

class Mamifero(Animal): 
    def __init__(self, volume_som: int, tamanho_passo: int):
        super().__init__(tamanho_passo)
        self.__volume_som = volume_som

    #@property irá possibilitar consultar dado de atributo privado. 
    @property
    def volume_som(self):
        return self.__volume_som


    # @nomeatributo.setter irá possibilitar a modificação do atributo privado.
    @volume_som.setter
    def volume_som(self,volume_som):
        self.__volume_som = volume_som

    def produzir_som(self):
        mensagem = "MAMIFERO: PRODUX SOM:" +  str(self.__volume_som) + "SOM:"
        return mensagem