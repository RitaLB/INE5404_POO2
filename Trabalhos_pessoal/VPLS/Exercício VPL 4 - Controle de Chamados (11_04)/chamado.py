from abstractChamado import AbstractChamado
from tipoChamado import TipoChamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class Chamado(AbstractChamado):
    def __init__(
        self,
        data: Date,
        cliente: Cliente,
        tecnico: Tecnico,
        titulo: str,
        descricao: str,
        prioridade: int,
        tipo: TipoChamado):

        self.__cliente = cliente
        self.__data = data
        self.__descricao = descricao
        self.__prioridade = prioridade
        self.__tecnico = tecnico
        self.__tipo = tipo
        self.__titulo = titulo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def data(self):
        return self.__data

    @property
    def descricao(self):
        return self.__descricao

    @property
    def prioridade(self):
        return self.__prioridade

    @property
    def tecnico(self):
        return self.__tecnico

    @property
    def tipo(self):
        return self.__tipo

    @property
    def titulo(self):
        return self.__titulo
