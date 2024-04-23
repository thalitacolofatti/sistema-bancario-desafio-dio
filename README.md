# Sistema Bancario - Desafio DIO - Bootcamp Python AI

## Desafio v1: criar um Sistema Bancário em Python. 

Inicialmente o sistema será para um usuário com três operações essenciais: depósito, saque e extrato. Para o saque, há limite de 3 operações e cada operação só pode sacar R$500.00. Somente pode sacar se houver saldo suficiente. Cada depósito e saque deve aparecer no extrato, além do saldo atual.

Adicionei a visualização no extrato de quantos saques restam.

## Desafio v2: otimizar o sistema com funções

Separar em funções as operações de depósito, saque e extrato existentes e criar 2 novas: cadastrar usuário (cliente) e cadastrar conta bancária. Pode adicionar outras funções que sejam pertinentes.

A função Saque com argumentos apenas por nome (*keyword only*)

A função Depósito com argumentos apenas por posição (*positional only*)

A função Extrato com argumentos por posição e nome (*positional only and keyword only*) 

A função Cadastrar usuário-cliente com nome, data de nascimento, CPF(cadastrados apenas uma vez e só com números) e endereço (a string deve estar no formato logradouro, número - bairro - cidade/sigla estado)

A função Criar conta deve armazenar em lista: agência (numero fixo 0001), número da conta (sequencial começando em 1) e usuário, que pode ter mais de uma conta, mas uma conta só pode ser de um usuário.

Mantive a visualização no extrato de quantos saques restam e alterei a função filtrar usuários mostrada no curso.

## Desafio v3: Modelar o sistema bancário em POO (arquivo desafiopythonPOO.py)

Foi atualizada a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários.

O código deveria seguir o modelo de classes UML abaixo:

![sistema_bancario_UML](https://github.com/thalitacolofatti/sistema-bancario-desafio-dio/assets/62973671/bb56edd9-9d26-422f-b5c3-2091bb0763a9)
