from abc import ABC, abstractmethod
from animal import Animal

class Ave(Animal):
    def __init__(self, tamanho_passo: int, altura_voo: int):
        super.__init__(tamanho_passo)
        self.__altura_voo = altura_voo

    #@property irá possibilitar consultar dado de atributo privado. 
    @property
    def altura_voo(self):
        return self.altura_voo

    # @nomeatributo.setter irá possibilitar a modificação do atributo privado.
    @altura_voo.setter
    def altura_voo(self, altura_voo):
        self.__altura_voo = altura_voo

    def mover(self):
        mensagem = "ANIMAL: DESLOCOU"+ str(self.__tamanho_passo) + "VOANDO"
        return mensagem

    
    def produzir_som(self):
        mensagem = "AVE: PRODUZ SOM:"
        return mensagem

    

    