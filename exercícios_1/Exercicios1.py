from math import *

"""# 1) codigo passo 1:
class Televisao:

    def __init__(self):
        self.ligada = False
        self.canal = 2
"""

"""
# código passo 2:
class Televisao:

    def __init__(self, tamanho, marca):
        self.ligada = False
        self.canal = 2

        self.tamanho = tamanho
        self.marca = marca

televisao1 = Televisao(50, "samsung")
televisao2 = Televisao(70, "LG")
print("Televisao 1:", televisao1.tamanho , televisao1.marca)
print( "Televisao 2:", televisao2.tamanho, televisao2.marca)
"""

"""
# código passo 3:

class Televisao:

    def __init__(self, tamanho, marca, canal):
        self.ligada = False
        self.canal = canal

        self.tamanho = tamanho
        self.marca = marca

    def muda_canal_para_cima(self):
        self.canal = self.canal + 1

    def muda_canal_para_baixo(self):
        self.canal = self.canal -1
"""

"""
# código passo 4:
class Televisao:
    canal_minimo = 1
    canal_maximo = 99
    def __init__(self, tamanho, marca, canal):
        self.ligada = False
        self.canal = canal

        self.tamanho = tamanho
        self.marca = marca

    def muda_canal_para_cima(self):
        if self.canal != self.canal_maximo:
            self.canal = self.canal + 1
        else:
            self.canal = self.canal_minimo
        
    def muda_canal_para_baixo(self):
        if self.canal != self.canal_minimo:
            self.canal = self.canal -1
        
        else: 
            self.canal = self.canal_maximo
"""
"""
#código passo 5:

class Televisao:

    def __init__(self, tamanho, marca, canal, canal_minimo = 2, canal_maximo = 14):
        self.ligada = False
        self.canal = canal

        self.tamanho = tamanho
        self.marca = marca

    def muda_canal_para_cima(self):
        if self.canal != self.canal_maximo:
            self.canal = self.canal + 1
        else:
            self.canal = self.canal_minimo
        
    def muda_canal_para_baixo(self):
        if self.canal != self.canal_minimo:
            self.canal = self.canal -1
        
        else: 
            self.canal = self.canal_maximo

"""

"""
# código passo 6:

class Televisao:

    def __init__(self, tamanho, marca, canal, canal_minimo = 2, canal_maximo = 14):
        self.ligada = False
        self.canal = canal

        self.tamanho = tamanho
        self.marca = marca

    def muda_canal_para_cima(self):
        if self.canal != self.canal_maximo:
            self.canal = self.canal + 1
        else:
            self.canal = self.canal_minimo
        
    def muda_canal_para_baixo(self):
        if self.canal != self.canal_minimo:
            self.canal = self.canal -1
        
        else: 
            self.canal = self.canal_maximo

televisao1 = Televisao(50, "Lg", 3, canal_minimo = 0, canal_maximo= 20 )
televisao2 = Televisao(70, "Samsung", 4, canal_minimo = 0, canal_maximo = 30)

"""
"""
# codigo warm up 7:

class estados:

    def __init__(self, nome, sigla, cidades = []):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades
        self.população = 0

    def calcular_população(self):
        for cidade in self.cidades:
           self.população += cidade.habitantes
        return self.população

class cidade:

    def __init__(self, nome, população):
        self.nome = nome 
        self.habitantes = população


caruaru = cidade("Caruaru", 370000)
recife = cidade("Recife", 1700000)
petrolina = cidade("Petrolina", 350000)
Olinda = cidade("Olinda",390000 )

florianopolis = cidade("Florianopolis", 520000)
blumenau = cidade("Blumenal", 360000)
turvo = cidade("Turvo",12990)
pomerode = cidade("Pomerode", 34561)
tubarão = cidade("Tubarão", 106422)


pernambuco = estados("Pernambuco","PE", [petrolina, recife, caruaru, Olinda] )
santa_catarina = estados("Samta Catarina", "SC",[ florianopolis, blumenau, tubarão, turvo, pomerode])
print(pernambuco.calcular_população())
print(santa_catarina.calcular_população())
"""

"""
# Código Warm UP 8:

class coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar_coordenadas(self):
        return self.x, self.y
        

    def calcular_distancia(self,x2, y2):
        dab = ((self.x - x2)**2 + (self.y - y2)**2) *1/2
        return dab

    def comparar_coordenada(self, x2, y2):
        if self.x == x2 and self.y == y2:
            return "Coordenadas iguais"

        else:
            return "coordenadas diferentes"

          

    def coordenada_polar(self):
        self.r = ((self.x**2 ) + (self.y**2))**1/2


        self.calcular_theta()

        return self.r ,self.theta

    def calcular_theta(self):

        if self.x >0 :
            self.theta = atan(self.y/self.x)

        elif self.x < 0 and self.y >= 0:
            self.theta = atan(self.y/self.x) + pi

        elif self.x <0 and self.y <0:
            self.theta = atan(self.y/self.x) - pi
        
        elif self.x ==0 and self.y >0:
            self.theta = pi/2

        elif self.x == 0 and self.y <0:
            self.theta = -pi /2

        else:
            self.theta = "Indefinido"

"""
"""
#código warm up 9:

#criando quadrados de cores iguais, mudando apenas o tamanho:
class quadrado:
    cor = "vermelho"
    def __init__(self, lado):
        self.lado = lado

        self.area = self.lado**2

class retangulo:
    cor  =  "vermelho"
    def __init__(self, comprimento, altura):
        self.comprimento = comprimento
        self.altura = altura
        self.area = self.comprimento * self.altura

class circulo:
    cor = "vermelho"
    def __init__(self, raio):
        self.raio = raio
        self.circunterência = 2*pi*self.raio
        self.area = pi* (self.raio**2)

"""
"""
#código warm up 10
#a) Implemente metodos para somas, subtração, multiplicação e divisão de duas frações

class fracao:
    def __init__(self, numerador, denominador):

        self.numerador = numerador
        self.denominador = denominador

    def somar(self, fracao2):

        soma = (self.numerador / self.denominador) + (fracao2.numerador/fracao2.denominador)
        return soma

    def subtrair(self, fracao2):
        subtracao = (self.numerador / self.denominador) - (fracao2.numerador/fracao2.denominador)
        return subtracao
    
    def multiplicar(self, fracao2):
        muntiplicao = (self.numerador / self.denominador) * (fracao2.numerador/fracao2.denominador)
        return muntiplicao

    def dividir(self, fracao2):
        divisao = (self.numerador / self.denominador) / (fracao2.numerador/fracao2.denominador)
        return divisao
    
"""

"""
#b)  Implemente o método que imprime uma fração no formato numerador / denominador
class fracao:
    def __init__(self, numerador, denominador):

        self.numerador = numerador
        self.denominador = denominador

    def somar(self, fracao2):

        soma = (self.numerador / self.denominador) + (fracao2.numerador/fracao2.denominador)
        return soma

    def subtrair(self, fracao2):
        subtracao = (self.numerador / self.denominador) - (fracao2.numerador/fracao2.denominador)
        return subtracao
    
    def multiplicar(self, fracao2):
        muntiplicao = (self.numerador / self.denominador) * (fracao2.numerador/fracao2.denominador)
        return muntiplicao

    def dividir(self, fracao2):
        divisao = (self.numerador / self.denominador) / (fracao2.numerador/fracao2.denominador)
        return divisao


    def imprimir_fracao(self):
      fracao = "{}/{}".format(self.numerador, self.denominador)
      return fracao

"""
"""
#c) Implemente um método que inverte a fração
class fracao:
    def __init__(self, numerador, denominador):

        self.numerador = numerador
        self.denominador = denominador

    def somar(self, fracao2):

        soma = (self.numerador / self.denominador) + (fracao2.numerador/fracao2.denominador)
        return soma

    def subtrair(self, fracao2):
        subtracao = (self.numerador / self.denominador) - (fracao2.numerador/fracao2.denominador)
        return subtracao
    
    def multiplicar(self, fracao2):
        muntiplicao = (self.numerador / self.denominador) * (fracao2.numerador/fracao2.denominador)
        return muntiplicao

    def dividir(self, fracao2):
        divisao = (self.numerador / self.denominador) / (fracao2.numerador/fracao2.denominador)
        return divisao


    def imprimir_fracao(self):
      fracao = "{}/{}".format(self.numerador, self.denominador)
      return fracao

    def inverter_fracao(self):
        numerador = self.numerador
        denominador = self.denominador
        self.denominador = numerador
        self.numerador = denominador
"""
"""
#d) Implemente um método que retorna a fração em valor real

class fracao:
    def __init__(self, numerador, denominador):

        self.numerador = numerador
        self.denominador = denominador

    def somar(self, fracao2):

        soma = (self.numerador / self.denominador) + (fracao2.numerador/fracao2.denominador)
        return soma

    def subtrair(self, fracao2):
        subtracao = (self.numerador / self.denominador) - (fracao2.numerador/fracao2.denominador)
        return subtracao
    
    def multiplicar(self, fracao2):
        muntiplicao = (self.numerador / self.denominador) * (fracao2.numerador/fracao2.denominador)
        return muntiplicao

    def dividir(self, fracao2):
        divisao = (self.numerador / self.denominador) / (fracao2.numerador/fracao2.denominador)
        return divisao


    def imprimir_fracao(self):
      fracao = "{}/{}".format(self.numerador, self.denominador)
      return fracao

    def inverter_fracao(self):
        numerador = self.numerador
        denominador = self.denominador
        self.denominador = numerador
        self.numerador = denominador
    
    def valor_real(self):
        ValorReal = self.numerador / self.denominador
        return ValorReal
"""

#e) Implemente um método que cria uma fração (numerador/denominador) a partir de um número real

class fracao:
    def __init__(self, numerador, denominador):

        self.numerador = numerador
        self.denominador = denominador

    def somar(self, fracao2):

        soma = (self.numerador / self.denominador) + (fracao2.numerador/fracao2.denominador)
        return soma

    def subtrair(self, fracao2):
        subtracao = (self.numerador / self.denominador) - (fracao2.numerador/fracao2.denominador)
        return subtracao
    
    def multiplicar(self, fracao2):
        muntiplicao = (self.numerador / self.denominador) * (fracao2.numerador/fracao2.denominador)
        return muntiplicao

    def dividir(self, fracao2):
        divisao = (self.numerador / self.denominador) / (fracao2.numerador/fracao2.denominador)
        return divisao


    def imprimir_fracao(self):
      fracao = "{}/{}".format(self.numerador, self.denominador)
      return fracao

    def inverter_fracao(self):
        numerador = self.numerador
        denominador = self.denominador
        self.denominador = numerador
        self.numerador = denominador
    
    def valor_real(self):
        ValorReal = self.numerador / self.denominador
        return ValorReal
    
    




    

     






    


