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


def incluir_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print('\n>>> Contato {} adicionado com sucesso! <<<\n'.format(contato))


mostrar_contatos()
#buscar_contato('Maria')
incluir_contato('Joao', '9993888811', 'joao@solyd.com.br', 'Av. 3')
mostrar_contatos()
