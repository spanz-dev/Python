class Produto:
    def __init__(self , produto , preco, quantidade_estoque):

        self.produto = produto
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def total_estoque(self):

        return  self.preco * self.quantidade_estoque
    
    def adicionar_estoque(self , quantidade):

        self.quantidade_estoque += quantidade

        return quantidade
    
    def remover_estoque(self , quantidade):

        self.quantidade_estoque -= quantidade

        return quantidade

p = Produto('mouse' , 50 , 5)

while True:
    print("""
    ===== MENU =====
    1 - Solicitar total do estoque
    2 - Adicionar estoque
    3 - Remover estoque
    4 - Sair
    ================
    """)

    opcao = input("escolha uma opção: ")

    if opcao == '1':

        print(f'''

            Esse é o total de seu estoque: {p.total_estoque()}

            ''')
    if opcao == '2':

        add = int(input('quantos produtos voce quer adicionar no estoque?'))

        p.adicionar_estoque(add)

        print(f'''

        Vôce adicionou {add} produtos no estoque!!!

        Agora tem {p.quantidade_estoque} em estoque!
        
        ''')
    if opcao == '3':

        sub = int(input('Digite quantos produtos voce quer remover do estoque>>'))

        p.remover_estoque(sub)

        print(f'''

        Voce retirou {p} do estoque!
              
        Agora tem apenas {p.quantidade_estoque} em estoque!

        ''')
    elif opcao == '4':
        print('Encerrando sistema...')
        break