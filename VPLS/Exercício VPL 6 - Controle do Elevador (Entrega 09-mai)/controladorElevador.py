from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador

class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = None

    @property
    def elevador(self):
        return self.__elevador

    def subir(self):
        self.__elevador.subir()

    def descer(self):
        self.__elevador.descer()

    def entraPessoa(self):
        self.__elevador.entraPessoa()

    def saiPessoa(self):
        self.__elevador.saiPessoa()

    def inicializarElevador(self, andarAtual, totalAndaresPredio, capacidade, totalPessoas):
        if type(andarAtual) != int or type(totalAndaresPredio) != int or type(capacidade) != int or type(totalPessoas) != int:
            raise ComandoInvalidoException
        elif andarAtual < 0 or totalAndaresPredio < 0 or capacidade < 0 or totalPessoas < 0:
            raise ComandoInvalidoException
        elif andarAtual >= totalAndaresPredio:
            raise ComandoInvalidoException
        elif totalPessoas > capacidade:
            raise ComandoInvalidoException
        else:
            self.__elevador = Elevador(capacidade, totalPessoas, totalAndaresPredio, andarAtual)
