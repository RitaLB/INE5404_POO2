from AbstractCarta import *
from Personagem import *


class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        self.__personagem = personagem

    '''
    Soma e retorna todos os valores dos atributos do personagem da Carta
    @return Retorna o somatorio de todos os atributos do personagem da Carta
    '''
    def valor_total_carta(self) -> int:
        e = self.__personagem.energia
        h = self.__personagem.habilidade
        v = self.__personagem.velocidade
        r = self.__personagem.resistencia
        soma = e + h + v + r
        return soma

    @property
    def personagem(self) -> Personagem:
        return self.__personagem
