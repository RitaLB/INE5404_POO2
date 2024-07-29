from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        self.__capitulos = [Capitulo(numeroCapitulo, tituloCapitulo)]

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def editora(self):
        return self.__editora
    
    @property
    def autores(self):
        return self.__autores

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo
    
    @ano.setter
    def ano(self, ano: int):
        self.__ano = ano
    
    @editora.setter
    def editora(self, editora: Editora):
        self.__editora = editora
    
    
    def incluirAutor(self, autor: Autor):
        if type(autor) == Autor:
            duplicado = False
            
            for i in self.__autores:
                if i == autor:
                    duplicado = True
            
            if duplicado == False:
                self.__autores.append(autor)

    def excluirAutor(self, autor: Autor):
        if type(autor) == Autor:
            for i in self.__autores:
                if i == autor:
                    self.__autores.remove(autor)
                    break

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        duplicado = False
        for i in self.__capitulos:
            if i.titulo == tituloCapitulo and i.numero == numeroCapitulo:
                duplicado = True
        
        if duplicado == False:
            capitulo = Capitulo(numeroCapitulo, tituloCapitulo)
            self.__capitulos.append(capitulo)

    def excluirCapitulo(self, tituloCapitulo: str):
        for i in self.__capitulos:
            if i.titulo == tituloCapitulo:
                self.__capitulos.remove(i)
                del i
                break
                
    def findCapituloByTitulo(self, tituloCapitulo: str):
        a = None
        for i in self.__capitulos:
            if i.titulo == tituloCapitulo:
                a = i
                break
        return a
