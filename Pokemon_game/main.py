import pickle

from pokemon import *
from pessoa import *

def escolher_pokemon_inicial(player):
    print('Olá {}, você poderá escolher agora o Pokemon que irá lhe acompanhar nessa jornada!'.format(player))

    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)

    print('Você tem 3 opções: ')
    print('1 - ', pikachu)
    print('2 - ', charmander)
    print('3 - ', squirtle)

    while True:
        escolha = input('Escolha o seu Pokemon: ')

        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print('Escolha inválida.')


def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
    except Exception as err:
        print('Erro ao salvar jogo.')
        print(err)


def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:
            player = pickle.load(arquivo)
            print('Jogo salvo carregado com sucesso!')
            return player
    except Exception as err:
        print('Erro ao carregar jogo salvo.')
        print(err)


if __name__ == '__main__':
    print('\n\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-')
    print('Bem-vindo ao game Pokemon RPG - Terminal Edition!!!')
    print('\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/- \n')

    player = carregar_jogo()

    if not player:

        nome = input('Olá, qual é o seu nome ?: ')
        player = Player(nome)
        print('Olá {}, este é um mundo terminal habitado por Pokemons, a partir de agora sua missão é se tornar um mestre dos Pokemons.'.format(nome))
        print('Capture o máximo de Pokemons que conseguir e lute com seus inimigos.')
        player.mostrar_dinheiro()

        if player.pokemons:
            print('Já vi que você tem alguns Pokemons.')
            player.mostrar_pokemons()
        else:
            print('Você não tem nenhum Pokemon, portanto precisa escolher um Pokemon inicial.')
            escolher_pokemon_inicial(player)
        
        print('Agora que você já possui um Pokemon, enfrente seu arquirrival Lawliet!')
        lawliet = Inimigo(nome='Lawliet', pokemons=[PokemonAgua('Squirtle', level=1)])
        player.batalhar(lawliet)

        salvar_jogo(player)

    while True:
        print('\n--------------------')
        print('O que deseja fazer?')
        print('1 - Explorar pelo mundo')
        print('2 - Lutar com um inimigo')
        print('3 - Ver sua coleção de Pokemons')
        print('0 - Sair do jogo')
        print('--------------------\n')
        escolha = input('Opção: ')

        if escolha == '0':
            print('Jogo encerrado.')
            break
        elif escolha == '1':
            player.explorar()

            salvar_jogo(player)
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            
            salvar_jogo(player)
        elif escolha == '3':
            player.mostrar_pokemons()
        else:
            print('Opção inválida.')