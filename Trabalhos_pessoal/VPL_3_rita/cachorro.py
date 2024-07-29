from animal import Animal
from mamifero import Mamifero

class cachorro(Mamifero):
    def __init__(self):
        super().__init__(3,3)

    def latir():
        mensagem = super().produzir_som() + "AU"

        