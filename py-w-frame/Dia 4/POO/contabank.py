class ContaBancaria:
    def __init__(self , titular):

        self.titular = titular
        self.saldo = 0

    def depositar(self , valor):
        if valor > 0:
            self.saldo += valor
            print(f"✔ Deposito de R$ {valor:.2f} realizado com sucesso")
        else:
            print("❌ Saldo insuficiente.")
    
    def sacar(self , valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"✔ Saque de R$ {valor:.2f} realizado.")
        else:
            print("❌ Saldo insuficiente.")
        
    def exibir_saldo(self):
        print(f"\n💰 Saldo atual de {self.titular}: R$ {self.saldo:.2f}\n")

titular = input("Digite o nome do titular da conta: ")
conta = ContaBancaria(titular)

while True:
    print("""
    ===== MENU =====
    1 - Depositar
    2 - Sacar
    3 - Ver saldo
    4 - Sair
    """)

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        valor = float(input("Digite o valor do depósito: "))
        conta.depositar(valor)
    elif opcao == '2':
        valor = float(input("Digite o valor do saque: "))
        conta.sacar(valor)
    elif opcao == '3':
        conta.exibir_saldo()
    elif opcao == '4':
        print("Encerrando sistema...")
        break
    else:
        print("❌ Opção inválida.")