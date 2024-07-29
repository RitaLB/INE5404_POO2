from pessoa import Pessoa
from calculadora_view import CalculadoraView
import PySimpleGUI as sg

class CalculadoraControlador:
    def __init__(self):
        self.__tela_calculadora = CalculadoraView(self)
        self.__pessoa = None
    
    def inicia(self):
        self.__tela_calculadora.tela_principal()


        #Loop de eventos
        rodando = True
        while rodando:
            event, values = self.__tela_calculadora.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == 'Calcular IMC':
                try:
                    peso = float(values['peso'])
                    altura = float(values['altura'])
                    self.__pessoa = Pessoa(peso, altura)
                    imc = self.__pessoa.calcular_imc()
                    if imc < 18.5:
                        classificacao = 'Baixo Peso'
                    elif imc < 25:
                        classificacao = 'Peso Normal'
                    elif imc < 30:
                        classificacao = 'Sobrepeso'
                    else:
                        classificacao = 'Obesidade'
                    self.__tela_calculadora.mostrar_resultado(imc, classificacao)

                except ValueError:
                    rodando = True
        