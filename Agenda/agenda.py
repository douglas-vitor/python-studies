AGENDA = {}

'''AGENDA['Guilherme'] = {
    'telefone': '9999999',
    'email': 'guigui@solyd.com.br',
    'endereco': 'Av. 1',
}

AGENDA['Maria'] = {
    'telefone': '99977779',
    'email': 'maria@solyd.com.br',
    'endereco': 'Av. 2',
}'''

def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('\n>>> Agenda vazia. <<<\n')


def buscar_contato(contato):

    try:
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
        print('-------------------------------------------\n')
    except KeyError:
        print('\n>>> Contato {} inexistente. <<<\n'.format(contato))
    except Exception as err:
        print('\n>>> Um erro inesperado aconteceu. <<<\n')
        print('>>> {}'.format(err))


def ler_detalhes_contato():
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereço do contato: ')
    return telefone, email, endereco


def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar()
    print('\n>>> Contato {} adicionado/editado com sucesso! <<<\n'.format(contato))


def excluir_contato(contato):

    try:
        AGENDA.pop(contato)
        salvar()
        print('\n>>> Contato {} excluído com sucesso! <<<\n'.format(contato))
    except KeyError:
        print('\n>>> Contato {} inexistente. <<<\n'.format(contato))
    except Exception as err:
        print('\n>>> Um erro inesperado aconteceu. <<<\n')
        print('>>> {}'.format(err))


def exportar_contatos(nome_do_arquivo):

    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write('{};{};{};{}\n'.format(contato,telefone,email,endereco))
        print('\n>>> Agenda exportada com sucesso! <<<\n')
    except:
        print('\n>>> Um erro ocorreu ao exportar contatos. <<<\n')


def importar_contatos(nome_do_arquivo):

    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(';')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                incluir_editar_contato(nome, telefone, email, endereco)
    except IOError:
        print('\n>>> Um erro ocorreu ao abrir arquivo. <<<\n')
    except FileNotFoundError:
        print('\n>>> Um erro ocorreu ao abrir arquivo. <<<\n')
    except Exception as err:
        print('\n>>> Um erro ocorreu ao importar contatos. <<<\n')
        print(err)


def salvar():
    exportar_contatos('database.csv')


def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(';')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }
        print('\n>>> Database carregada com sucesso! <<<')
        print('>>> {} Contatos carregados! <<<\n'.format(len(AGENDA)))
    except IOError:
        print('\n>>> Um erro ocorreu ao abrir database. <<<\n')
    except FileNotFoundError:
        print('\n>>> Um erro ocorreu ao abrir database. <<<\n')
    except Exception as err:
        print('\n>>> Um erro ocorreu ao carregar database. <<<\n')
        print(err)


def imprimir_menu():
    print('1 - Mostrar todos os contatos da agenda.')
    print('2 - Buscar contato.')
    print('3 - Incluir contato.')
    print('4 - Editar contato.')
    print('5 - Excluir contato.')
    print('6 - Exportar contatos para CSV.')
    print('7 - Importar contatos CSV.')
    print('0 - Fechar agenda.')
    print('-------------------------------------------\n')


carregar()
while True:
    imprimir_menu()

    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)
    elif opcao == '3':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('\n>>> Contato: {} já existe. <<<\n'.format(contato))
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)

    elif opcao == "4":
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('\n>>> Editando contato: {}. <<<\n'.format(contato))
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print('\n>>> Contato {} não existe. <<<\n'.format(contato))

    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser salvo: ')
        exportar_contatos(nome_do_arquivo)
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser aberto: ')
        importar_contatos(nome_do_arquivo)
    elif opcao == '0':
        print('\n>>> Fechando programa! <<<\n')
        break
    else:
        print('\n>>> Opção inválida. <<<\n')