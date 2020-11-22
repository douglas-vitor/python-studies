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
        print('Nome:', contato)
        print("Telefone:", AGENDA[contato]["telefone"])
        print("Email:", AGENDA[contato]["email"])
        print("Endereço:", AGENDA[contato]["endereco"])
        print('-------------------------------------------\n')


mostrar_contatos()