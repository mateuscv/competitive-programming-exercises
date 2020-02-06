class Alunos:

    numero_de_alunos = 0
    coeficiente_aluno = 8

    def __init__(self, nome, matricula, status):
        self.matricula = matricula
        self.nome = nome
        self.status = status
        Alunos.numero_de_alunos += 1
    
    def aprovarAluno(self):
        self.status = 'Aprovado'
        self.coeficiente_aluno += 1

aluno1 = Alunos("Mateus Vieira", "116514", "Reprovado")
aluno2 = Alunos("Dief Mendes", "123456", "Aprovado")
aluno1.aprovarAluno()
print(aluno1.nome + ", Status: " + aluno1.status + ", Coeficiente: " + str(aluno1.coeficiente_aluno))
print(aluno2.nome + ", Status: " + aluno2.status + ", Coeficiente: " + str(aluno2.coeficiente_aluno))

