'''
Escreva um programa em python que realize o gerenciamento de jogadores. Ele deve atender aos seguintes requisitos:

- Adicionar um time
- Remover um time
- Listar times
- Adicionar jogador em um time
- Remover jogador de um time
- Listar jogadores de um time
1. A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.
2. A opção de adicionar um time deve pedir um nome para o time que será cadastrado.
3. A opção de remover um time deve pedir o índice específico do time que foi cadastrado para fazer a sua exclusão.
4. A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar com o nome do jogador que será adicionado.
5. A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador que fora cadastrado no time.
6. A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.

Este é o exercício de revisão do módulo, então aproveite para utilizar todos os recursos vistos até agora, como os funções, condições, loop, listas, etc.
'''
import sys
import os
import time

listaTimes = {}
programa_ativo = True

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def animacao_carregamento():
    frase = "Aguarde"
    pontos = "..."
    
    for _ in range(3):  # Quantidade de vezes que a animação será repetida
        for i in range(len(pontos) + 1):
            sys.stdout.write("\r" + frase + "." * i + ' ' * (len(pontos)-i))  # Imprime a frase e os pontos
            sys.stdout.flush()  # Limpa o buffer de stdout
            time.sleep(0.5)  # Pausa antes da próxima atualização

def impressaoListaDeTimes():
    print('='*4, 'LISTA DE TIMES', '='*4, '\n')
    for i in range(len(listaTimes)):
        print(f"{i}-{listaTimes[i]}")

    print("\n" + "="*20)

def adicionaTime():
    opcaoAdicionaTime = input("Deseja continuar(S/N): ").strip().lower()
    limpar_tela()

    while opcaoAdicionaTime not in ['s', 'n']: 
        print("Erro! Digite apenas S ou N")
        opcaoAdicionaTime = input("Deseja continuar(S/N): ").strip().lower()
        limpar_tela()

    if opcaoAdicionaTime in ['s']:
        limpar_tela()
        nome = input("Qual o nome do time que deseja adicionar: ")
        nome = nome[0].upper() + nome[1:].lower()
        times = {'nome': nome}
        listaTimes[nome] = times
        limpar_tela()

        if listaTimes[nome]:
            print(f"{nome} criado com sucesso!\n")
            animacao_carregamento()
            limpar_tela()
        else:
            print("Erro ao criar o time.\n")
            print("-"*5, " Aguarde ", "-"*5)
            animacao_carregamento()
            limpar_tela()
    else:
        escolha()

def removerTime():
    chaves = list(listaTimes.keys())
    
    if not chaves:
        print("Não há times cadastrados para remover.")
        animacao_carregamento()
        limpar_tela()
        escolha()
        return

    opcaoRemoveTime = input("Deseja continuar(S/N): ").strip().lower() 
    limpar_tela()
    
    while opcaoRemoveTime not in ['s', 'n']: 
        opcaoRemoveTime = input("Erro! Digite apenas S ou N\n").strip().lower()
        limpar_tela()

    if opcaoRemoveTime in ['s']:
        remocao = input('Digite I para deletar pelo indice e N pelo nome do time: ').strip().lower()
        limpar_tela()

        while remocao not in ['i', 'n']:
            remocao = input('Erro! Digite apenas I ou N: ').strip().lower()
        
        limpar_tela()

        if remocao in ['i']:
            impressaoListaDeTimes()
            indice = int(input('\nDigite o índice do time que deseja excluir: '))

            while indice <= 0 or indice > len(chaves):
                impressaoListaDeTimes()
                indice = int(input("Insira um indice válido: "))
                limpar_tela()

            nome_do_time = chaves[indice]
            confirmacao = input(f"Tem certeza que deseja excluir o time {nome_do_time}? (S/N): ").strip().lower()
            limpar_tela()

            while confirmacao not in ['s', 'n']: 
                confirmacao = input("Erro! Digite apenas S ou N\n").strip().lower()
                limpar_tela()

            if confirmacao == 's':
                del listaTimes[nome_do_time]
                if nome_do_time not in listaTimes:
                    print(f"{nome_do_time} removido com sucesso.\n")
                    animacao_carregamento()
                    limpar_tela()
                else:
                    print("\nFalha na exclusão!\n")
                    animacao_carregamento()
                    limpar_tela()
            else:
                print("Operação cancelada pelo usuário.")
                animacao_carregamento()
                limpar_tela()

        elif remocao in ['n']:
            impressaoListaDeTimes()
            nome = input('\nDigite o nome do time que deseja excluir: ')
            limpar_tela()

            if isinstance(nome, int):
                while isinstance(nome, int):
                    impressaoListaDeTimes()
                    nome = input('\nNome inválido. Por favor insira um nome válido: ')
                    limpar_tela()   
            elif nome not in listaTimes:
                while nome not in listaTimes:
                    impressaoListaDeTimes()
                    nome = input('\nNome inválido. Por favor insira um nome válido: ')
                    limpar_tela()
            
            confirmacao = input(f"Tem certeza que deseja excluir o time {nome}? (S/N): ").strip().lower()
            limpar_tela()

            while confirmacao not in ['s', 'n']: 
                confirmacao = input("Erro! Digite apenas S ou N\n").strip().lower()
                limpar_tela()

            if confirmacao == 's':
                del listaTimes[nome]
                if nome not in listaTimes:
                    print(f"{nome} removido com sucesso.\n")
                    animacao_carregamento()
                    limpar_tela()
                else:
                    print(f"Ocorreu um erro ao tentar remover {nome}.\n")
                    animacao_carregamento()
                    limpar_tela()
                    escolha()
            else:
                print("Operação cancelada pelo usuário.")
                animacao_carregamento()
                limpar_tela()
                escolha()  
        escolha()

def listaTimes():
    if not listaTimes:  # Verifica se a lista de chaves está vazia
        print("Não há times cadastrados.")
        time.sleep(3)
        escolha()
    else:
        impressaoListaDeTimes()
        voltar = int(input("\nAperte 1 para voltar: "))
        limpar_tela()

        while voltar != 1:
            voltar = int(input("\nOpção Inválida.Digite 1: "))
            limpar_tela()

        if voltar == 1:
            limpar_tela()

def escolha():
    global programa_ativo
    while programa_ativo:
        try:
            print('='*7, 'MENU', '='*7, '\n')
            opcao = int(input("1-Adicionar um time\n2-Remover um time\n3-Listar times\n4-Adicionar jogador em um time\n5-Remover jogador de um time\n6-Listar jogadores de um time\n7-Fechar programa\n\nOpção Escolhida: "))

            if opcao >= 1 and opcao <= 6:
                if opcao == 1:
                    limpar_tela()
                    adicionaTime()
                elif opcao == 2:
                    limpar_tela()
                    removerTime()
                elif opcao == 3:
                    limpar_tela()
                    listaTimes()
            elif opcao == 7:
                programa_ativo = False
                limpar_tela()
                print("Programa encerrado.")
            else:
                limpar_tela()

        except ValueError:
            limpar_tela()

limpar_tela()
escolha()