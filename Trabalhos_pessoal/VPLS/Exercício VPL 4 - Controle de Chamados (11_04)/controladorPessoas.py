from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self):
        return self.__clientes

    @property
    def tecnicos(self):
        return self.__tecnicos

    def incluiCliente(self, codigo: int, nome: str):
        cliente = Cliente(nome, codigo)
        duplicado = False
        for c in self.__clientes:
            if codigo == c.codigo:
                duplicado = True
                break

        if not duplicado:
            self.__clientes.append(cliente)
            return cliente
        else:
            return None

    def incluiTecnico(self, codigo: int, nome: str):
        tecnico = Tecnico(nome, codigo)
        duplicado = False
        for t in self.__tecnicos:
            if t.codigo == codigo:
                duplicado = True
                break

        if not duplicado:
            self.__tecnicos.append(tecnico)
            return tecnico
        else:
            return None
