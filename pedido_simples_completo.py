lista = []

print('Sejam Bem Vindos na Nossa Hamburgueria Tem Pra todos! E Já Venho Agradeser Pela Preferencia.')

print()

print('Hamburguer')
x_tudo = print('X-Tudo: R$12,00')
hamburguer = print('Hamburguer: R$7,00')
x_burgue = print('X-Buguer: R$9,00')
x_bacon = print('X-Bacon: R$14,00')
x_calabresa = print('X-Calabresa: R$14,00')
x_duplo = print('X-Duplo: R$15,00')
x_triplo = print('X-Triplo: R$18,00')

print()

print('Batata')
batata_pp = print('Batata-PP: R$5,00')
batata_p = print('Batata-P: R$8,00')
batata_maluca = print('Batata-Maluca: R$20,00')

print()

print('Bebidas')
coca_cola = print('Cola-Cola Lata: R$7,00')
coca_cola2 = print('cola-cola 2 Litro: R$12,00')
pepsi = print('Pepsi Lata: R$5,00')
kuat = print('Kuat 2 Litro: R$8,00')
quara_vita = print('quara vita: R$2,00')

print()

print('Combo casal')
combo_casal = print('Combo-Casal: R$35,00, Vem com 2 x-tudo, batata-frita calabresa, bacon, cheddar e queijo ralado')
combo_trio = print('Combo-Trio: 45,00, Vem com 3 x-tudo, batata-frita calabresa, bacon, cheddar e queijo ralado')

print()

while True:
    print('1 - Escolha o seu pedido do cardapio:')
    print('2 - Lista sou pedido:')
    print('3 - Editar pedido:')
    print('4 - Excluir pedido:')
    print('5 - Sair')

    print()

    opcao = input('Escolha uma opção a cima: ')

    print()

    if opcao == '1':
        print('---------- Cadastro e Pedidos ----------')
        print()

        nome = input('Me enforme o seu nome: ')
        telefone = int(input('Informe um numero pra contato: '))
        rua = input('Me informe sua rua: ')
        numero = int(input('Numero do endereço: '))
        bairro = input('Bairro: ')
        pedido = input('Qual seria o seu pedido: ')

        print()

        lista.append({'nome': nome, 'telefone': telefone, 'rua': rua, 'numero': numero, 'bairro': bairro, 'pedido': pedido})

        print()

    elif opcao == '2':
        print('----------- Lista do Pedido ----------')
        print()

        for idx, listas in enumerate(lista):
            print(f'ID: {idx}')
            print(f'Nome: {listas["nome"]}')
            print(f'Telefone: {listas["telefone"]}')
            print(f'rua: {listas["rua"]}')
            print(f'Numero: {listas["numero"]}')
            print(f'Bairro: {listas["bairro"]}')
            print(f'Pedido: {listas["pedido"]}')
            print()

        print()

    elif opcao == '3':
        print('----------- Editar Pedido ----------')
        print()

        id_pedido = int(input('Informe o ID do pedido que deseja editar: '))
        novo_pedido = input('Informe o novo pedido: ')

        if 0 <= id_pedido < len(lista):
            lista[id_pedido]['pedido'] = novo_pedido
            print('Pedido editado com sucesso!')
        else:
            print('ID do pedido inválido.')

        print()

    elif opcao == '4':
        print('----------- Excluir Pedido ----------')
        print()

        id_pedido = int(input('Informe o ID do pedido que deseja excluir: '))

        if 0 <= id_pedido < len(lista):
            del lista[id_pedido]
            print('Pedido excluído com sucesso!')
        else:
            print('ID do pedido inválido.')

        print()

    elif opcao == '5':
        print('Sair do Pedido...')
        break

    else:
        print('Opção incorreta!')

print()

print('Pedido Finalisado.')
