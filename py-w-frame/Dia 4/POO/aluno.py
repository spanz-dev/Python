class Aluno():
    def __init__(self , nome , matricula ):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self , nota):

        self.notas.append(nota)

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        media = self.calcular_media()
        if media > 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"
            
aluno1 = Aluno("Enzo" , "2026001")

aluno1.adicionar_nota(6.5)
aluno1.adicionar_nota(7.0)
aluno1.adicionar_nota(8.0)

print(f'''

        Aluno : {aluno1.nome}
        Media : {aluno1.calcular_media()}
        Situação : {aluno1.situacao()}

     ''')
