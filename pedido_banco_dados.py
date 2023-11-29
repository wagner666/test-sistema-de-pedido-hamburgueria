import sqlite3

# Conecte-se ao banco de dados (isso criará um novo arquivo de banco de dados se ele não existir)
conn = sqlite3.connect('hamburgueria.db')

# Crie um objeto cursor para executar consultas SQL
cursor = conn.cursor()

# Crie uma tabela para armazenar os pedidos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        telefone INTEGER,
        rua TEXT,
        numero INTEGER,
        bairro TEXT,
        pedido TEXT
    )
''')

# Confirme as alterações e feche a conexão
conn.commit()
conn.close()

# Agora você pode usar o banco de dados em seu programa
lista = []

print('Sejam Bem Vindos na Nossa Hamburgueria Tem Pra todos! E Já Venho Agradecer Pela Preferência.')
print()

while True:
    print('1 - Escolha o seu pedido do cardápio:')
    print('2 - Lista seu pedido:')
    print('3 - Editar pedido:')
    print('4 - Excluir pedido:')
    print('5 - Sair')
    print()

    opcao = input('Escolha uma opção acima: ')
    print()

    if opcao == '1':
        print('---------- Cadastro e Pedidos ----------')
        print()

        nome = input('Me informe o seu nome: ')
        telefone = int(input('Informe um número para contato: '))
        rua = input('Me informe sua rua: ')
        numero = int(input('Número do endereço: '))
        bairro = input('Bairro: ')
        pedido = input('Qual seria o seu pedido: ')

        conn = sqlite3.connect('hamburgueria.db')
        cursor = conn.cursor()

        # Insira o pedido no banco de dados
        cursor.execute('''
            INSERT INTO pedidos (nome, telefone, rua, numero, bairro, pedido)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nome, telefone, rua, numero, bairro, pedido))

        conn.commit()
        conn.close()

        print()

    elif opcao == '2':
        print('----------- Lista do Pedido ----------')
        print()

        conn = sqlite3.connect('hamburgueria.db')
        cursor = conn.cursor()

        # Busque e exiba todos os pedidos do banco de dados
        cursor.execute('SELECT * FROM pedidos')
        orders = cursor.fetchall()

        for order in orders:
            print(f'ID: {order[0]}')
            print(f'Nome: {order[1]}')
            print(f'Telefone: {order[2]}')
            print(f'Rua: {order[3]}')
            print(f'Número: {order[4]}')
            print(f'Bairro: {order[5]}')
            print(f'Pedido: {order[6]}')
            print()

        conn.close()

    elif opcao == '3':
        print('----------- Editar Pedido ----------')
        print()

        conn = sqlite3.connect('hamburgueria.db')
        cursor = conn.cursor()

        # Busque e exiba todos os pedidos do banco de dados
        cursor.execute('SELECT * FROM pedidos')
        orders = cursor.fetchall()

        for order in orders:
            print(f'ID: {order[0]}')
            print(f'Nome: {order[1]}')
            print(f'Telefone: {order[2]}')
            print(f'Rua: {order[3]}')
            print(f'Número: {order[4]}')
            print(f'Bairro: {order[5]}')
            print(f'Pedido: {order[6]}')
            print()

        order_id = int(input('Informe o ID do pedido que deseja editar: '))
        novo_pedido = input('Informe o novo pedido: ')

        # Atualize o pedido no banco de dados
        cursor.execute('UPDATE pedidos SET pedido = ? WHERE id = ?', (novo_pedido, order_id))
        conn.commit()
        conn.close()


    elif opcao == '4':
        print('----------- Excluir Pedido ----------')
        print()

        conn = sqlite3.connect('hamburgueria.db')
        cursor = conn.cursor()

        # Busque e exiba todos os pedidos do banco de dados
        cursor.execute('SELECT * FROM pedidos')
        orders = cursor.fetchall()

        for order in orders:
            print(f'ID: {order[0]}')
            print(f'Nome: {order[1]}')
            print(f'Telefone: {order[2]}')
            print(f'Rua: {order[3]}')
            print(f'Número: {order[4]}')
            print(f'Bairro: {order[5]}')
            print(f'Pedido: {order[6]}')
            print()

            order_id = int(input('Informe o ID do pedido que deseja excluir: '))

            # Exclua o pedido do banco de dados
            cursor.execute('DELETE FROM pedidos WHERE id = ?', (order_id,))
            conn.commit()
            conn.close()

    elif opcao == '5':
        print('Sair do Pedido...')
        break

    else:
        print('Opção incorreta!')

print()
print('Pedido Finalizado.')
