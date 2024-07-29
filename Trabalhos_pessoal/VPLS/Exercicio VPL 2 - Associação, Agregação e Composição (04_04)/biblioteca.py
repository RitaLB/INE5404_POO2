from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluirLivro(self, livro: Livro):
        if type(livro) == Livro:
            duplicado = False
            for i in self.__livros:
                if i.codigo == livro.codigo:
                    duplicado = True
            
            if duplicado == False:
                self.__livros.append(livro)

    def excluirLivro(self, livro: Livro):
        if type(livro) == Livro:
            for i in self.__livros:
                if i.codigo == livro.codigo:
                    self.__livros.remove(livro)

    @property
    def livros(self):
        return self.__livros
