
class Aluno():

    def __init__(self,nome="nome",nota=[], semestre=1) -> None:
        self.__nome = nome
        self.nota = nota
        self.semestre = semestre


    #Substitui a função embutida do print()
    def __repr__(self):
        return  self.__nome + " nota: " + str(self.nota) + " semestre: " + str(self.semestre)

#Só a titulo de curiosidade
def construtor(classe):
    return classe()


alunos = {}
for x in range(10):
    alunos[str(x)]= Aluno("nome"+ str(x),[]) 
print(alunos)
print('------')
# modifica e adiciona aluno
alunos['0'].nota = 999

alunos['paulo'] = Aluno("paulo",[1,2,3],3)
print(alunos)

alunos['paulo'].nota.append(57)
print(alunos)

# Cria aluno com função
aluno = construtor(Aluno)
print(aluno)