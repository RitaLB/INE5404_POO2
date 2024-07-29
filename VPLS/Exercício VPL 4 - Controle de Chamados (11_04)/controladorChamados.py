from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__tipoChamados = []
        self.__chamados = []
  
    @property
    def tipoChamados(self):
        return self.__tipoChamados

    def incluiTipoChamado(self, codigo: int, nome: str, descricao: str):
        tipo = TipoChamado(codigo, descricao, nome)
        duplicado = False
        for t in self.__tipoChamados:
            if t.codigo == codigo:
                duplicado = True
                break

        if not duplicado:
            self.__tipoChamados.append(tipo)
            return tipo
        else:
            return None

    def incluiChamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado):
        if isinstance(data, Date) and isinstance(cliente, Cliente) and isinstance(tecnico, Tecnico) and isinstance(tipo, TipoChamado):
            chamado = Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)
            duplicado = False
            for c in self.__chamados:
                if c.data == data and c.cliente == cliente and c.tecnico == tecnico and c.tipo == tipo:
                    duplicado = True

            if not duplicado:
                self.__chamados.append(chamado)
                return chamado
        else:
            return None

    def totalChamadosPorTipo(self, tipo: TipoChamado):
        soma = 0
        for c in self.__chamados:
            if c.tipo.codigo == tipo.codigo:
                soma += 1
        return soma
