from abstractTipoChamado import AbstractTipoChamado


class TipoChamado(AbstractTipoChamado):
    def __init__(self, codigo: int, descricao: str, nome: str):
        self.__codigo = codigo
        self.__nome = nome
        self.__descricao = descricao

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def nome(self):
        return self.__nome
