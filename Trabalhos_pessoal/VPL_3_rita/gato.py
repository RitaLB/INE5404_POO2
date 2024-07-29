from mamifero import Mamifero

class Gato(Mamifero):
    def __init__(self):
        super().__init__(2,2)

    def miar():
        mensagem = super().produzir_som() + "MIAU"