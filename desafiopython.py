menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite por saque.")
        
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
            
    elif opcao == "e":
        print("\n==============Extrato==============\n")
        print("Não foram realizadas movimentações\n" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print(f"\nResta(m) {LIMITE_SAQUES-numero_saques} saque(s).\n" if saldo > 0 else "")
        print("===================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
