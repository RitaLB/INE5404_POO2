
class Aluno():

    def __init__(self,nome,nota) -> None:
        self.__nome = nome
        self.nota = nota

    def __repr__(self):
        return  self.__nome + " nota: " + str(self.nota)


alunos = {}
for x in range(10):
    alunos[str(x)]= Aluno("nome"+ str(x),[]) 

alunos['0'].nota = 999

alunos['paulo'] = Aluno("paulo",[1,2,3])

print(alunos)

alunos['paulo'].nota.append(57)
print(alunos)