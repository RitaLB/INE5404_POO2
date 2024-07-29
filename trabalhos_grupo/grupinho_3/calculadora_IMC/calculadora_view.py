import PySimpleGUI as sg

class CalculadoraView:
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = []
        self.__window = None


    def tela_principal(self):
        
        linha0 = [sg.Text('Qual seu peso?'), sg.InputText('', key = 'peso'), sg.Text('kg')]
        linha1 = [sg.Text('Qual sua altura?'), sg.InputText('', key = 'altura'), sg.Text('m')]
        linha2 = [sg.Text('Seu IMC é'), sg.Text('', key = 'imc', size = (6, 1))]
        linha3 = [sg.Text('Classificação:'), sg.Text('', key = 'classificacao')]
        linha4 = [sg.Text('', size = (14, 1)), sg.Button('Calcular IMC')]
        self.__container = [linha0, linha1, linha2, linha3, linha4]
        self.__window = sg.Window('Calculadora de IMC', self.__container, font=('Helvetica', 14))

    def le_eventos(self):
        return self.__window.read()

    #def fim(self):
        #self.__window.close()

    def mostrar_resultado(self, imc, classificacao):
        self.__window.Element('imc').Update(imc)
        self.__window.Element('classificacao').Update(classificacao)
    

