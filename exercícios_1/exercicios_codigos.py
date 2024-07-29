"""Exercício 1: Banco
O banco Tatu, moderno e eficiente, precisa de um novo programa para controlar o saldo de
seus correntistas. Cada conta corrente pode ter um ou mais clientes como titular. O banco
controla apenas o nome e o telefone de cada cliente. A conta corrente apresenta um saldo e
uma lista de operações de saques e depósitos. Quando o cliente fizer um saque, diminuiremos
o saldo da conta corrente. Quando ele fizer um depósito, aumentaremos o saldo. O banco
oferece também contas especiais, com limite especial além do saldo, e conta poupança, que
oferece um rendimento mensal sempre que o saldo na conta completa um mês. Evidentemente
é necessário oferecer aos clientes a possibilidade de verificar saldos, extratos e um resumo
com todas as informações da conta e seus respectivos clientes.
"""
"""
class conta_corrente:

    def __init__(self, tipo_de_conta, saldo_inicial, clientes = []):
        self.clientes = clientes
        self.tipo_de_conta = tipo_de_conta
        self.saldo_inicial = saldo_inicial
        self.saldo = saldo_inicial
        self.limite = self.definir_limite()

        self.meuextrato = []
    
    def definir_limite(self):
        
        if self.tipo_de_conta == "Carbon":
            return 20000
        if self.tipo_de_conta == "Gold":
            return  10000
    
        elif self.tipo_de_conta == "Silver":
            return 7000
    
        elif self.tipo_de_conta == "Basic":
            return 0
                

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.meuextrato.append("Saque: -{};".format(valor))
        else:
            print("Erro: Não é possível realizar saque. Valor ultrapassa limite da conta")

    def deposito(self, valor):
        self.saldo += valor
        self.meuextrato.append("Depósito: {};".format(valor))

    def verificar_saldo(self):
        print(self.saldo)

    def extrato(self):
        print("Saldo inicial: {}".format(self.saldo_inicial))
        for movimento in self.meuextrato:
            print(movimento)
        print("Saldo Atual: {}".format(self.saldo))

    def informacoes_conta(self):
        inf_da_conta = "Tipo de conta: {},  Limite: {}, Clintes: {} ".format(self.tipo_de_conta, self.limite, self.clientes)
        print(inf_da_conta)


    

class cliente:
    def __init__(self,nome, telefone):
        self.nome = nome
        self.telefone = telefone
"""

"""Exercício 10: Organização das Turmas
Crie um sistema que gerencia o cadastro de alunos e professores em turmas. Os usuários
serão os membros da secretaria. Eles devem conseguir visualizar os alunos matriculados em
cada turma, com seus dados, suas notas e presenças. Além disso, os secretários precisam ter
acesso a dados cadastrais dos professores associados à disciplina"""

class professor:
    def __main__(self, nome, ID, disciplinas, area_pesquisa):
        self.nome = nome
        self.ID = ID
        self.disciplinas = disciplinas
        self.area_pesquisa = area_pesquisa

class aluno:
    def __main__(self, nome, ID, turmas):
        self.nome = nome
        self.ID = ID
        self.turmas = turmas

    def add_nota(self, curso, nota):
        pass


class curso:
    def __main__(self, nome):
        self.nome = nome
        self.notas = []
        self.faltas = []

    


