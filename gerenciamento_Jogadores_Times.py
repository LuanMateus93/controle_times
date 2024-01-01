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
    chaves = list(ordenaDicionario().keys())
    
    print('='*4, 'LISTA DE TIMES', '='*4, '\n')
    for i in range(len(chaves)):
        print(f"{i}-{chaves[i]}")

    print("\n" + "="*23)

def ordenaDicionario():
    listaTimesOrdenada = dict(sorted(listaTimes.items(), key=lambda item: item[0]))

    return listaTimesOrdenada

def limpar_entrada():
    if sys.stdin.isatty():
        try:
            # Para sistemas Unix/Linux
            import termios
            termios.tcflush(sys.stdin, termios.TCIOFLUSH)
        except ImportError:
            # Para Windows (Apenas uma tentativa, pode não funcionar conforme esperado)
            import msvcrt
            while msvcrt.kbhit():
                msvcrt.getch()

def adicionaTime():

    nome = input("Qual o nome do time que deseja adicionar: ")
    nome = nome[0].upper() + nome[1:].lower()
    limpar_tela()

    confirmacao = input(f"Tem certeza que quer adicionar {nome}?(S/N): ").strip().lower()
    limpar_tela()

    while confirmacao not in ['s', 'n']: 
        confirmacao = input("Erro! Digite apenas S ou N: ").strip().lower()
        limpar_tela()

    if confirmacao == 's':
        if nome not in listaTimes:
            try:
                limpar_tela
                listaTimes[nome] = {'nome': nome}
                limpar_tela()

                print(f"{nome} criado com sucesso!\n")
                animacao_carregamento()
                limpar_tela()
            except Exception as e:
                print("Erro ao criar o time.\n")
                print(f"Erro: {e}\n")
                animacao_carregamento()
                limpar_tela()
        else:
            print('Este time já existe na lista.\n')
            animacao_carregamento()
            limpar_tela()
            escolha()
    else:
        limpar_tela()
        animacao_carregamento()
        limpar_tela()

def removerTime():
    impressaoListaDeTimes()
    nome = input('\nDigite o nome do time que deseja excluir: ')
    limpar_tela()
    
    confirmacao = input(f"Tem certeza que deseja excluir o time {nome}? (S/N): ").strip().lower()
    limpar_tela()

    while confirmacao not in ['s', 'n']: 
        confirmacao = input("Erro! Digite apenas S ou N\n").strip().lower()
        limpar_tela()

    if confirmacao == 's':
        try:
            del listaTimes[nome]
            
            print(f"{nome} removido com sucesso.\n")
            animacao_carregamento()
            limpar_tela()
            escolha()
        except KeyError:
            print(f"O time {nome} não existe na lista e não pode ser removido.Retornando ao menu principal\n")
            animacao_carregamento()
            limpar_tela()
            escolha()
        except Exception as e:
            print(f"Ocorreu um erro ao tentar remover {nome}: {e}.Retornando ao menu principal\n")
            animacao_carregamento()
            limpar_tela()
            escolha()
    else:
        limpar_tela()
        animacao_carregamento()
        limpar_tela()


def listarTimes():
    if not listaTimes:
        print("Não há times cadastrados.")
        voltar = input("\nAperte Enter para voltar: ")
        limpar_tela()

        while voltar != '':
            voltar = int(input("\nOpção Inválida.Aperte Enter: "))
            limpar_tela()
    else:
        impressaoListaDeTimes()
        voltar = input("\nAperte Enter para voltar: ")
        limpar_tela()

        while voltar != '':
            voltar = int(input("\nOpção Inválida.Aperte Enter: "))
            limpar_tela()

def adicionarJogadores():
    listaTimes = ordenaDicionario()

    if listaTimes:
        impressaoListaDeTimes()
        timeJogador = input("\nQual o nome do time que deseja adicionar o jogador: ")
        limpar_tela()
        
        while timeJogador not in listaTimes:
            impressaoListaDeTimes()
            timeJogador =  input('\nERRO! O time não existe. Digite um time válido: ')
            limpar_tela()

        jogador = input("Insira o nome do jogador a ser adicionado: ")
        jogador = jogador[0].upper() + jogador[1:].lower()
        limpar_tela()

        confirmacao = input(f"Tem certeza que deseja adicionar o jogador {jogador} ao time {timeJogador}? (S/N): ").strip().lower()
        limpar_tela()

        while confirmacao not in ['s', 'n']: 
            confirmacao = input("Erro! Digite apenas S ou N\n").strip().lower()
            limpar_tela()

        if confirmacao == 's':
            try:
                if 'players' not in listaTimes[timeJogador]:
                    listaTimes[timeJogador]['players'] = []
                    
                if jogador in listaTimes[timeJogador]['players']:  
                    print(f'{jogador} já existe no time {timeJogador}!!! Voltando ao menu principal')
                    animacao_carregamento()
                    limpar_tela()
                else:
                    listaTimes[timeJogador]['players'].append(jogador)
                    listaTimes[timeJogador]['players'] = sorted(listaTimes[timeJogador]['players'])
                    print(f"Jogador {jogador} adicionado com sucesso ao time {timeJogador}!")
                    limpar_tela()
            except Exception as e:
                print(f"Ocorreu um erro ao tentar adicionar {jogador} ao time {timeJogador}: {e}.Retornando ao menu principal\n")
                animacao_carregamento()
                limpar_tela()
                escolha()
        else:
            print('Você escolheu voltar ao menu principal!!!')
            animacao_carregamento()
            limpar_tela()
    else:
        print('Nenhum time cadastrado!!!\n')
        animacao_carregamento()
        limpar_tela()

def removerJogadores():
    listaTimes = ordenaDicionario()

    if listaTimes:
        impressaoListaDeTimes()
        timeJogador = input("\nQual o nome do time que deseja remover o jogador: ")
        limpar_tela()

        while timeJogador not in listaTimes:
            impressaoListaDeTimes()
            timeJogador = input('\nERRO! O time não existe. Digite um time válido: ')
            limpar_tela()

        if 'players' in listaTimes[timeJogador] and listaTimes[timeJogador]['players']:
            jogadoresOrdenados = sorted(listaTimes[timeJogador]['players'])
            print(f"Jogadores do time {timeJogador} em ordem alfabética:\n")
            for i in range(len(jogadoresOrdenados)):
                print(f'{i}-{jogadoresOrdenados}')
            jogador = input("\nInsira o nome do jogador a ser removido: ")
            jogador = jogador[0].upper() + jogador[1:].lower()

            if jogador in listaTimes[timeJogador]['players']:
                confirmacao = input(f"Tem certeza que deseja remover o jogador {jogador} do time {timeJogador}? (S/N): ").strip().lower()
                limpar_tela()
                
                while confirmacao not in ['s', 'n']:
                    confirmacao = input("Erro! Digite apenas S ou N: ").strip().lower()
                    limpar_tela()

                if confirmacao == 's':
                    listaTimes[timeJogador]['players'].remove(jogador)
                    print(f"Jogador {jogador} removido com sucesso do time {timeJogador}!")
                else:
                    print(f"Remoção do jogador {jogador} cancelada.")
            else:
                print(f"Jogador {jogador} não encontrado no time {timeJogador}.")
        else:
            print(f"Não há jogadores para remover no time {timeJogador}.")
    else:
        print('Nenhum time cadastrado!!!')
        animacao_carregamento()
        limpar_tela()

def imprimirJogadores():
    listaTimes = ordenaDicionario()

    if listaTimes:
        impressaoListaDeTimes() 
        timeEscolhido = input("\nInsira o nome do time para ver a lista de jogadores em ordem alfabética: ")
        limpar_tela()

        while timeEscolhido not in listaTimes:
            impressaoListaDeTimes()
            timeEscolhido = input('\nERRO! O time não existe. Por favor, digite um time válido: ')
            limpar_tela()

        if 'players' in listaTimes[timeEscolhido] and listaTimes[timeEscolhido]['players']:
            jogadoresOrdenados = sorted(listaTimes[timeEscolhido]['players'])
            print(f"Jogadores do time {timeEscolhido} em ordem alfabética:\n")
            for i in range(len(jogadoresOrdenados)):
                print(f'{i}-{jogadoresOrdenados}')
            
            voltar = input("\nAperte Enter para voltar: ")
            limpar_tela()

            while voltar != '':
                voltar = int(input("\nOpção Inválida.Aperte Enter: "))
                limpar_tela()

            animacao_carregamento()
            limpar_tela()
        else:
            print(f"Não há jogadores cadastrados no time {timeEscolhido}.")
            animacao_carregamento()
            limpar_tela()
    else:
        print('Nenhum time cadastrado!!!')
        animacao_carregamento()
        limpar_tela()

def escolha():
    global programa_ativo
    while programa_ativo:
        try:
            limpar_entrada()
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
                    listarTimes()
                elif opcao == 4:
                    limpar_tela()
                    adicionarJogadores()
                elif opcao == 5:
                    limpar_tela()
                    removerJogadores()
                elif opcao == 6:
                    limpar_tela()
                    imprimirJogadores()
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