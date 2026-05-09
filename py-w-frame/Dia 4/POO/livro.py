class Livro:
    def __init__(self , titulo="" , autor="" , ano=0 , disponivel=True):

        self.livro = []
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel

    def listar_livro(self):
        if not self.livro:
             print('nunhum livro cadastrado')
             return
        print("===== LISTA DE LIVROS =====")
        for livro in self.listar_livro:
             status = "Disponível" if livro["disponivel"] else "Emprestado"
             print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Status: {status}")
        print("===========================")
             
         


    def info(self):
        if self.livro:
            return f"Título: {self.livro[0]}, Autor: {self.livro[1]}, Ano: {self.livro[2]}"
        else:
            return "Nenhum livro cadastrado."

meus_livros = Livro()

while True:
        print("""
        ===== MENU DA LIVRARIA =====
        1 - listar livro
        2 - Emprestar
        3 - Devolver
        4 - Info dos livros
        5 - Sair
        """)

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            lvr_titulo = input("Digite o titulo do livro: ")
            lvr_autor = input('Digite o autor do livro: ')
            Lvr_ano = int(input('Digite o ano em que esse livro foi lançado: '))
            meus_livros.listar_livro(lvr_titulo , lvr_autor , Lvr_ano)
            print(f'O livro {lvr_titulo} foi cadastrado!')
        elif opcao == '4':
             Livro.info()