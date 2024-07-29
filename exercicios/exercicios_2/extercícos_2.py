"""#Exercício 6. ​ Faça um Programa que peça as quatro notas de 10 alunos, calcule e
#armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

class Turma:
    def __init__(self, id, n_provas, alunos = None):
        self.id_turma = id
        self.alunos = alunos
        self.numero_provas = n_provas

        if self.alunos is None:
            self.alunos = []

class Aluno:
    def __init__(self,nome):
        #variável nome
        self.nome = nome
        #vetor turmas
        self.turmas = []
        #dicionário de notas:
        #cada chve do dicionário (com o ID da turma) mapeia para uma lista com as notas do aluno
        self.notas = {}
        self.medias = {}

    #função para armazenar nota na lista atrelada ao id da matéria específica
    def armazenar_nota(self, turma, nota):
        id_turma = turma.id_turma
        self.notas[id_turma].append(nota)
        self.calcular_media(turma, nota)


    def calcular_media(self, turma, nota):
        id_turma = turma.id_turma
        soma = 0
        for nota in self.notas[id_turma]:
            soma += int(nota)
        media = soma/ turma.numero_provas
        self.medias[id_turma] = media
        return media

#classe para gerenciar a entrada e a saída de alunos de turmas
class operacoes_turmas:
    def __init__(self):
        pass

    #função para pegar ID turma (melhorar legibilidade do código):
    def get_turma_id(self, turma):
        return turma.id_turma


    def inserir_turma(self,  aluno, turma):

        #adicionar turma na lista de turmas do objeto aluno
        aluno.turmas.append(turma)

        #adicionar chave e lista vazia atrelada à chave para a turma no dicionário de notas:
        id_turma = self.get_turma_id(turma)
        aluno.notas[id_turma]= []

        #adicionar o aluno na lista de alunos do objeto turma
        turma.alunos.append(aluno)
        
# criando uma turma:
turma1 = Turma("turma1", 4)

#Criando a lista com 10 alunos:
Lista_alunos = []*10
for i in range (10):
    Lista_alunos.append( Aluno("Aluno"+ str(i)))

#inserindo alunos na turma1:
for aluno in Lista_alunos:
    operacoes_turmas().inserir_turma(aluno, turma1)

# pedindo as 4 notas e inserindo elas nas instâncias dos alunos:
for aluno in Lista_alunos:
    notas = input("Digite as 4 notas do {}\n".format(aluno.nome)).split()
    while len(notas) != 4:
        print("Número de notas incorreto")
        notas = input("Digite as 4 notas do {}\n".format(aluno.nome)).split()

    for nota in notas:
        aluno.armazenar_nota(turma1, nota)

#verificando a quantidade de alunos com media >= 7:

alunos_aprovados = 0
for aluno in Lista_alunos:
    if aluno.medias[turma1.id_turma] >= 7:
        alunos_aprovados += 1

print("A turma 1 tem {} alunos aprovados (Com média maior ou igual a 7.0)".format(alunos_aprovados))

"""
"""
#Exercício 7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

class vetornum:
    def __init__(self, quantidade):
        self.quantidade = quantidade
        self.vetor = []
        self.soma = 0
        self.multiplicacao = 0

    #função para criar vetor com a quantidade específica de numeros
    def criar_vetor(self):
        self.vetor = input("Digite {} numeros inteiros\n".format(self.quantidade)).split()
        if len(self.vetor) != self.quantidade:
          print("Vetor não possui {} números".format(self.quantidade))
          self.criar_vetor()

        #realizando altomaticamente cálculos:
        self.fazer_calculos()
    #função para calcular soma e multiplicação:
    def fazer_calculos(self):
        #calculando soma:
        for numero in self.vetor:
            self.soma += int(numero)

        #calculando multiplicação:
        multiplicacao = int(self.vetor[0])
        for i in range(1, len(self.vetor)):
            multiplicacao = multiplicacao * int(self.vetor[i])
        
        self.multiplicacao = multiplicacao

    # função para mostrar números do vetor:
    def mostrar_vetor (self):
        print("Os números do vetor são:", end =" ")
        for numero in self.vetor:
            print(numero, end = " ")

vetor1 = vetornum(4)
vetor1.criar_vetor()

print("A soma dos números do vetor é:", vetor1.soma)
print("A multiplicação do números do vetor 1 é:", vetor1.multiplicacao)
vetor1.mostrar_vetor()

"""

"""
# Exercício 9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule 
#e mostre a soma dos quadrados dos elementos do vetor.

class vetornum:
    def __init__(self, quantidade):
        self.quantidade = quantidade
        self.vetor = []

    #função para criar vetor com a quantidade específica de numeros
    def criar_vetor(self):
        self.vetor = input("Digite {} numeros inteiros\n".format(self.quantidade)).split()
        if len(self.vetor) != self.quantidade:
          print("Vetor não possui {} números".format(self.quantidade))
          self.criar_vetor()


    #função para rmostrar os números do vetor:
    def mostrar_vetor (self):
        print("Os números do vetor são:", end =" ")
        for numero in self.vetor:
            print(numero, end = " ")

#criando vetor:
vetorA = vetornum(10)
vetorA.criar_vetor()

#calculando a operação pedida:
soma_quadrados=  0
for numero in vetorA.vetor:
    soma_quadrados += int(numero)**2

#mostrando o resultado:
print("A soma dos quadrados dos números do Vetor A =", soma_quadrados)
"""


#  Exercício 14
"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
○ "Telefonou para a vítima?"
○ "Esteve no local do crime?"
○ "Mora perto da vítima?"
○ "Devia para a vítima?"
○ "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no
crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário,
ele será classificado como "Inocente"""
"""
class investigado:
    def __init__(self, nome):
        self.nome = nome
        self.classificacao = ""
        self.pontos = 0
        self.respostas = []

        self.perguntas = [
            "Telefonou para a vítima?",
            "Esteve no local do crime?",
            "Mora perto da vítima?",
            "Devia para a vítima?",
            "Já trabalhou com a vítima?"]
        
    def contar_pontos(self, i=0):

        print("Responda as seguintes perguntas com 'SIM' ou 'NAO' \n")
        while i <= len(self.perguntas)-1:
            print(i)
            resposta = input("{} ".format(self.perguntas[i]))
            
            if resposta != "SIM" and resposta != "NÃO":
                print("Resposta não reconhecida. Verificar digitação")
                self.contar_pontos(i)

            else: 
                i += 1
                self.respostas.append(resposta)

    def classificar(self):
        self.contar_pontos()
        for resposta in self.respostas:
            if resposta == "SIM":
                self.pontos += 1

        print("Número de pontos:", self.pontos)

        if self.pontos == 2:
            self.classificacao = "Suspeita"
        
        elif self.pontos == 3 or self.pontos == 4:
            self.classificacao = "Cúmplice"

        elif self.pontos == 5:
            self.classificacao = "Assassino"

        else:
            self.classificacao = "Inocente"

pessoa1 = investigado("joão")
pessoa1.classificar()
print(pessoa1.classificacao)

"""

"""
Exercício 13. Faça um programa que receba a temperatura média de cada mês do ano
e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e
mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""

#criar classe para armazenar dados e realizar métodos de ocmparação
class ano:
    def __init__(self):
        self.meses = ["Janeiro", "Fevereiro", 
                      "Março", "Abril", 
                      "Maio", "Junho", 
                      "Julho", "Agosto", 
                      "Setembro", "Outubro", 
                      "Novembro", "Dezembro"]
        
        self.temperaturas = []
        self.media_anual = 0

    #método para realizar operações pedidas de uma só vez
    def rodar_programa(self):
        self.get_temperaturas()
        self.calc_media()
        self.comparar_temperaturas()

    #método para receber temperaturas
    def get_temperaturas(self):
        for i in range (len(self.meses)):
            temperatura = input("Digite a temperatura média do mês de {} \n".format(self.meses[i]))
            self.temperaturas.append(temperatura) 

    #metodo para calcular média anual
    def calc_media(self):
        soma = 0
        for temperatura in self.temperaturas:
            soma += int(temperatura)

        self.media_anual = soma/12

    #método para comparar temperaturas

    def comparar_temperaturas(self):
        for i in range(len(self.temperaturas)):
            if int(self.temperaturas[i]) > self.media_anual:
                print(self.temperaturas[i], "-", self.meses[i], end ="; ")

#instanciar ano e rodar programa:
ano_2020 = ano()
ano_2020.rodar_programa()
    


            
           

