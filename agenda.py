AGENDA = {}

AGENDA['Guilherme'] = {
    'telefone': '9999999',
    'email': 'guigui@solyd.com.br',
    'endereco': 'Av. 1',
}

AGENDA['Maria'] = {
    'telefone': '99977779',
    'email': 'maria@solyd.com.br',
    'endereco': 'Av. 2',
}


def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)


def buscar_contato(contato):
    print('Nome:', contato)
    print('Telefone:', AGENDA[contato]['telefone'])
    print('Email:', AGENDA[contato]['email'])
    print('Endereço:', AGENDA[contato]['endereco'])
    print('-------------------------------------------\n')


def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print('\n>>> Contato {} adicionado/editado com sucesso! <<<\n'.format(contato))


def excluir_contato(contato):
    AGENDA.pop(contato)
    print('\n>>> Contato {} excluído com sucesso! <<<\n'.format(contato))


def imprimir_menu():
    print('1 - Mostrar todos os contatos da agenda.')
    print('2 - Buscar contato.')
    print('3 - Incluir contato.')
    print('4 - Editar contato.')
    print('5 - Excluir contato.')
    print('0 - Fechar agenda.')


opcao = input('Escolha uma opção: ')

if opcao == '1':
    mostrar_contatos()
elif opcao == '2':
    contato = input('Digite o nome do contato: ')
    buscar_contato(contato)
elif opcao == '3' or opcao == '4':
    contato = input('Digite o nome do contato: ')
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereço do contato: ')

    incluir_editar_contato(contato, telefone, email, endereco)
elif opcao == '5':
    contato = input('Digite o nome do contato: ')

    excluir_contato(contato)
elif opcao == '0':
    print('Fechando programa!')
else:
    print('Opção inválida.')