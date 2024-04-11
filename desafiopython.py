import textwrap

def menu():
    menu = """\n
===============Menu===============

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [u]\tNovo usuário
    [c]\tNova conta
    [l]\tListar contas

    [q]\tSair

=> """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor: .2f}\n"
        print("\n$$ Depósio realizado com sucesso! $$")
    else:
        print("\n** Operação falhou! O valor informado é inválido. **")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    saque_realizado = False
    
    if excedeu_saldo:
        print("\n** Operação falhou! Saldo insuficiente. **")

    elif excedeu_limite:
        print("\n** Operação falhou! O valor do saque excede o limite por saque.**")
    
    elif excedeu_saques:
        print("\n** Operação falhou! Número máximo de saques excedido. **")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor: .2f}\n"
        numero_saques += 1
        saque_realizado = True
        print("\n$$ Saque realizado com sucesso! $$")

    else:
        print("\n** Operação falhou! O valor informado é inválido. **")
    
    return saldo, extrato, saque_realizado

def mostrar_extrato(saldo, /, *, extrato, resta_saques):
    print("\n==============Extrato==============\n")
    print("Não foram realizadas movimentações\n" if not extrato else extrato)
    print(f"Saldo:\t\tR$ {saldo:.2f}")
    print(f"\nResta(m) {resta_saques} saque(s).\n" if saldo > 0 else "")
    print("===================================")

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("\n**Já existe usuário com esse CPF!**")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("== Usuário criado com sucesso! ==")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n== Conta criada com sucesso! ==")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("** Usuário não encontrado! **")

def listar_contas(contas):
    print(contas)
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            Conta:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, saque_realizado = sacar(
                saldo=saldo,
                valor=valor, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES)
            
            if saque_realizado:
                numero_saques += 1

        elif opcao == "e":
            resta_saques = LIMITE_SAQUES - numero_saques
            mostrar_extrato(saldo, extrato=extrato, resta_saques=resta_saques)

        elif opcao == "u":
            cadastrar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("** Operação inválida, por favor selecione novamente a opção desejada. **")

main()