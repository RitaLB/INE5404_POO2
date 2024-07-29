from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(self, capacidade, totalPessoas, totalAndaresPredio, andarAtual):
        self.__capacidade = capacidade
        self.__totalPessoas = totalPessoas
        self.__totalAndaresPredio = totalAndaresPredio
        self.__andarAtual = andarAtual

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def totalPessoas(self):
        return self.__totalPessoas

    @property
    def totalAndaresPredio(self):
        return self.__totalAndaresPredio

    @property
    def andarAtual(self):
        return self.__andarAtual

    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio):
        self.__totalAndaresPredio = totalAndaresPredio

    @totalPessoas.setter
    def totalPessoas(self, totalPessoas):
        self.__totalPessoas = totalPessoas

    @capacidade.setter
    def capacidade(self, capacidade):
        self.__capacidade = capacidade

    @andarAtual.setter
    def andarAtual(self, andarAtual):
        self.__andarAtual = andarAtual

    def subir(self):
        if self.__andarAtual == self.__totalAndaresPredio - 1:
            raise ElevadorJahNoUltimoAndarException
        else:
            self.__andarAtual += 1
            return 'O elevador subiu um andar.'

    def descer(self):
        if self.__andarAtual == 0:
            raise ElevadorJahNoTerreoException
        else:
            self.__andarAtual -= 1
            return 'O elevador desceu um andar.'

    def entraPessoa(self):
        if self.__totalPessoas == self.__capacidade:
            raise ElevadorCheioException
        else:
            self.__totalPessoas += 1
            return 'Uma pessoa entrou no elevador.'

    def saiPessoa(self):
        if self.__totalPessoas == 0:
            raise ElevadorJahVazioException
        else:
            self.__totalPessoas -= 1
            return 'Uma pessoa saiu do elevador.'
