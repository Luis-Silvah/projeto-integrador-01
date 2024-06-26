# Import Biblioteca Oracle
import oracledb

# Criacao da Conexao com o Banco de Dados
connection = oracledb.connect(
    user = 'BD150224213',
    password = 'Hhqnm9',
    dsn = '172.16.12.14/xe',
)

# Criacao da tabela no OrableDB
cursor = connection.cursor()
cursor.execute('DROP TABLE produto')

cursor.execute("""
                CREATE TABLE produto(
                nome  VARCHAR2(255) NOT NULL ,
                descricao VARCHAR2(255),
                codigo VARCHAR2(30) NOT NULL PRIMARY KEY,
                custo INTEGER NOT NULL,
                custoFixo INTEGER NOT NULL,
                comissao INTEGER NOT NULL,
                imposto INTEGER NOT NULL,
                rentabilidade NUMBER NOT NULL 
                )"""
)

# Inserts inicias na tabela
def insert_produtos():
    cursor.execute(""" 
                INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade) 
                VALUES ('Caneta', 'TIKQYQTHIVHWNMITKL', '1', 36, 15, 5, 12, 20)
    """)

    cursor.execute(""" 
                    INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade) 
                    VALUES ('Lapis', 'THCRVW', '2', 1, 1, 1, 1, 1)
    """)

    cursor.execute("""
                    INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade) 
                    VALUES ('Caderno', 'THCRVW', '3', 10, 10, 10, 10, 50)
                    """)

    cursor.execute("""
                    INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade) 
                    VALUES ('Caderno', 'THCRVW', '4', 10, 10, 10, 10, 0)
                    """)

    cursor.execute("""
                    INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade) 
                    VALUES ('Caderno', 'THCRVW', '5', 10, 10, 10, 10, -20)
                    """)

    cursor.execute("""
                    INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade) 
                    VALUES ('Caderno', 'THCRVW', '6', 10, 30, 20, 20, 29.99)
                    """)

    connection.commit()

insert_produtos()
tabela_alfabeto = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
def descriptografia(descProduto):
    chaveDescriptografia = [[45, -30], [-195, 165]]
    textoDescriptografado = ''

    descProdutoList = list(descProduto)

    # Se o comprimento da lista for ímpar, adiciona o último caractere novamente
    if len(descProdutoList) % 2 != 0:
        descProdutoList.append(descProdutoList[-1])
    
    listaPalavra = []
    listaNumeros = []

    for letraPalavra in descProdutoList:
        for numAlfabeto in range(len(tabela_alfabeto)):
            if letraPalavra == tabela_alfabeto[numAlfabeto]:
                if(letraPalavra == 'Z'):
                    listaPalavra.append(0)
                else:
                    listaPalavra.append(numAlfabeto)
                
    matrizPalavra = [listaPalavra[i:i+2] for i in range(0, len(listaPalavra), 2)]
    
    resultado_descriptografia = multiplicacao_matrizes(chaveDescriptografia,matrizPalavra)
    resultado_descriptografia = pmodulo_lista(resultado_descriptografia,26)

    for i in range(len(resultado_descriptografia)):
        for k in resultado_descriptografia[i]:
            listaNumeros.append(k)
    
    for num in listaNumeros:
        for numAlfabeto in range(len(tabela_alfabeto)):
            if num == numAlfabeto:
                if numAlfabeto == 0:
                    textoDescriptografado += 'Z'
                else:
                    textoDescriptografado += tabela_alfabeto[numAlfabeto]
    if textoDescriptografado[-1] == textoDescriptografado[-2]:
        textoDescriptografado = textoDescriptografado[:-1]
    
    return textoDescriptografado

def exibir_menu():
    print(36 * "=")
    print("Menu:")
    print(36 * "=")
    print("1. Adicionar novo produto")
    print("2. Selecionar um produto")
    print("3. Listar produtos")
    print("4. Deletar produto")
    print("5. Atualizar produto")
    print("6. Sair")
    print(36 * "-")
    
def verifica_produto(selecionaProduto):
    resultado = cursor.execute(f"SELECT * FROM PRODUTO WHERE codigo = '{selecionaProduto}'")

    produto_encontrado = False

    for lista in resultado:
        produto_encontrado = True

    return produto_encontrado

def pmodulo_lista(lista, divisor):
    restos = []
    for sublista in lista:
        resto_sublista = []
        for num in sublista:
            resto = num % divisor
            resto_sublista.append(resto)
        restos.append(resto_sublista)
    return restos

def multiplicacao_matrizes(chaveCriptografia, matrizPalavra):
    if len(matrizPalavra[0]) != len(chaveCriptografia):
        print("Número de colunas em A não é igual ao número de linhas em B.")
        return None

    result = [[0 for _ in range(len(chaveCriptografia[0]))] for _ in range(len(matrizPalavra))]

    # Realiza a multiplicação de matrizes
    for i in range(len(matrizPalavra)):
        for j in range(len(chaveCriptografia[0])):
            for k in range(len(chaveCriptografia)):
                result[i][j] += matrizPalavra[i][k] * chaveCriptografia[k][j]

    return result

def criptografia(descProduto):
    chaveCriptografia = [[11, 2], [13, 3]]   
    textoCriptografado = ''  
    
    descProdutoList = list(descProduto)

    # Se o comprimento da lista for ímpar, adiciona o último caractere novamente
    if len(descProdutoList) % 2 != 0:
        descProdutoList.append(descProdutoList[-1])
    
    listaPalavra = []
    listaNumeros = []

    for letraPalavra in descProdutoList:
        for numAlfabeto in range(len(tabela_alfabeto)):
            if letraPalavra == tabela_alfabeto[numAlfabeto]:
                if(letraPalavra == 'Z'):
                    listaPalavra.append(0)
                else:
                    listaPalavra.append(numAlfabeto)
                
    matrizPalavra = [listaPalavra[i:i+2] for i in range(0, len(listaPalavra), 2)]
    
    resultado_criptografia = multiplicacao_matrizes(chaveCriptografia, matrizPalavra)
    resultado_criptografia= pmodulo_lista(resultado_criptografia,26)
    
    for item in resultado_criptografia: 
        for k in item:
            listaNumeros.append(k)
            
    for num in listaNumeros:
        for numAlfabeto in range(len(tabela_alfabeto)):
            if num == numAlfabeto:
                if numAlfabeto == 0:
                    textoCriptografado += 'Z'
                else:
                    textoCriptografado += tabela_alfabeto[numAlfabeto]
    
    return textoCriptografado

def adicionar_produto():
    print(36 * "=")
    print("\t Sistema de Cadastro")
    print(36 * "=")

    codProduto = input("Digite o código do produto: ")
 
    if(verifica_produto(codProduto)):
        print('\n Já existe um produto com esse codigo \n')
    else:
        nomeProduto = input("Digite o nome do produto: ")
        descProduto = input("Adicione uma descrição ao produto: ").upper()
        descProduto = criptografia(descProduto)
        custoProduto = float(input("Qual o custo do Produto: "))
        custoFixoPct = float(input("Qual os custo fixos/administrativos do comércio [%]: "))
        comissaoVendaPct = float(input("Qual a comissão de venda do produto,em porcentagem [%]: "))
        impostoVendaPct = float(input("Qual a aliquota de imposto desejada [%]: "))
        margemLucroPct = float(input("Qual a margem de lucro desejada [%]: "))

        listaProduto = []
        listaProduto.append([nomeProduto,descProduto, codProduto, custoProduto, custoFixoPct, comissaoVendaPct, impostoVendaPct, margemLucroPct])
    
        cursor.execute(f""" 
                    INSERT INTO produto (nome, descricao, codigo, custo, custoFixo, comissao, imposto, rentabilidade) 
                    VALUES ('{nomeProduto}', '{descProduto}', '{codProduto}', {custoProduto}, {custoFixoPct}, {comissaoVendaPct}, {impostoVendaPct}, {margemLucroPct})
                """)
        connection.commit()
        
        tabela_produto(listaProduto[0])

        print('\n Cadastro concluído com sucesso! \n')

def selecionar_produto():
    selecionaProduto = input('Digite o código do produto: ')

    resultado = cursor.execute(f"SELECT * FROM PRODUTO WHERE codigo = '{selecionaProduto}'")

    produto_encontrado = False
    for lista in resultado:
        produto_encontrado = True
        tabela_produto(lista)
    
    if not produto_encontrado:
        print("\n Não foi possivel encontrar produto! \n")

def listar_produto():
    resultado = cursor.execute(f'SELECT * FROM PRODUTO ORDER BY codigo ASC')

    for lista in resultado:
        tabela_produto(lista)

def deletar_produto():
    codProduto = input('Digite o código do produto: ')

    if(verifica_produto(codProduto)):
        confirma = input('Digite o código do produto: S/N: ').upper()

        while confirma != "S" and confirma != "N":
            print("Digite S (Sim) e N (Não): ")
            confirma = input('Digite o código do produto: S/N: ').upper()
        else: 
            if confirma == "S":
                cursor.execute(f"""
                    DELETE FROM produto WHERE codigo = {codProduto}
                """)

                connection.commit()

                print("\n Produto deletado com sucesso! \n")
            # else: 
            #     print("\n Não deletar produto \n")
    else:
        print("\n Erro ao deletar produto! \n")

# Menu de opções possiveis para atualizar o produto
def menu_editarProduto(prod):
    print(40 * "=")
    print("Menu editar produto:")
    print(40 * "=")
    print(f"1. Nome: \t\t {prod[0]}")
    print(f"2. Descrição: \t\t {descriptografia(prod[1])}")
    print(f"3. Código: \t\t\t {prod[2]}")
    print(f"4. Custo: \t\t\t {prod[3]}")
    print(f"5. Custo Fixo/Administrativo: \t {prod[4]}")
    print(f"6. Comissão: \t\t\t {prod[5]}")
    print(f"7. Imposto: \t\t\t {prod[6]}")
    print(f"8. Rentabilidade: \t\t {prod[7]}")
    print(40 * "-")

# Atualiza os campos do produto
def atualizar_tabela(column, codProduto):
        valor = input("Digite o novo valor: ")

        cursor.execute(f"""
            UPDATE produto SET {column} = '{valor}' WHERE codigo = '{codProduto}'
        """)
        connection.commit()
        print("Produto atualizado com sucesso!")

# Recebe a opção do menu editar produto e direciona na função para atualizaro o campo
def editar_produto():
    codProduto = input('Digite o código do produto: ')

    if(verifica_produto(codProduto)):
        buscarProduto = cursor.execute(f"SELECT * FROM produto WHERE codigo = '{codProduto}'")

        for lista in buscarProduto:
            menu_editarProduto(lista)

        opcao = input("Escolha uma opção: ")
                
        if opcao == "1":
            atualizar_tabela('nome', codProduto)
        elif opcao == "2":
            descProduto = input("Digite a descrição do produto: ").upper()
            descProduto = criptografia(descProduto)

            cursor.execute(f"""
                UPDATE produto SET descricao = '{descProduto}' WHERE codigo = {codProduto}
            """)
            connection.commit()
            print("Produto atualizado com sucesso")
        elif opcao == "3":
            novoCodigoProduto = input('Digite o código do produto: ')

            if(verifica_produto(novoCodigoProduto)):
                print("\n Já existe um produto com esse código: \n")
            else: 
                cursor.execute(f"""
                    UPDATE produto SET codigo = '{novoCodigoProduto}' WHERE codigo = {codProduto}
                """)
                connection.commit()
                print("Produto atualizado com sucesso")
        elif opcao == "4":
            atualizar_tabela('custo', codProduto)
        elif opcao == "5":
            atualizar_tabela('custoFixo', codProduto)
        elif opcao == "6":
            atualizar_tabela('comissao', codProduto)
        elif opcao == "7":
            atualizar_tabela('imposto', codProduto)
        elif opcao == "8":
            atualizar_tabela('rentabilidade', codProduto)
        else:
            print("\n Opção inválida. Tente novamente. \n ") 
    else: 
        print("Produto não encontrado!")

# Campos da tabela PRODUTO

# [0] - nome 
# [1] - descricao
# [2] - codigo
# [3] - custo
# [4] - custoFixo
# [5] - comissao
# [6] - imposto
# [7] - rentabilidade

# Formata os dados e mostra na tabela o produto
def tabela_produto(tabela):
    # Campos
        nomeBD = tabela[0]
        descricaoDB = descriptografia(tabela[1])
        codigoDB = tabela[2]
        custoProdutoBD = tabela[3]
        custoFixoBD = tabela[4]
        comissaoVendaPctBD = tabela[5]
        impostoVendaPctBD =tabela[6]
        margemLucroPctBD = tabela[7]
    
        # Margem de lucro < 100
        if margemLucroPctBD < 100:
            # Preço de venda produto
            precoVenda = custoProdutoBD / (
            1 - ((custoFixoBD + comissaoVendaPctBD + impostoVendaPctBD + margemLucroPctBD) / 100)
             )
        else:
            # Preço de venda produto
            precoVenda = custoProdutoBD + ((custoFixoBD + comissaoVendaPctBD + impostoVendaPctBD + margemLucroPctBD)*custoProdutoBD / 100) 
        
        receitaBruta = precoVenda - custoProdutoBD # Receita Bruta

        comissaoVenda = comissaoVendaPctBD * precoVenda / 100 # Comissão de vendas 
        custoFixo = custoFixoBD * precoVenda / 100 # Custo fixo 
        impostoVenda = impostoVendaPctBD * precoVenda / 100 # Imposto

        outrosCustos = custoFixo + comissaoVenda + impostoVenda # Outros custos

        rentabilidade = receitaBruta - outrosCustos # Rentabilidade

        precoVendaPct = 100 * precoVenda / precoVenda # Preço de venda  %
        custoProdutoPct = custoProdutoBD * 100 / precoVenda # Custo produto %
        receitaBrutaPct = 100 * receitaBruta / precoVenda # Receita bruta  %
        outrosCustosPct = 100 * outrosCustos / precoVenda # Outros custos %

        rentabilidadePct = rentabilidade * 100 / precoVenda # Rentabilidade %

        # Tabela
        print('\n')
        print(64 * "=")

        print(f"Nome {nomeBD:^50}")

        print(f"Descrição {descricaoDB:^51}")

        print(f"Codigo {codigoDB:^51}")

        print(64 * "-")
        print(f"Descrição {'Valor':^51} {'[%]':^2}")
        print(64 * "-")
        print(f"Preço de Venda: {precoVenda:^40.2f} {precoVendaPct:7.0f}") 
        print(f"Custo de Aquisição (Fornecedor): {custoProdutoBD:^2.2f} {custoProdutoPct:^48.0f}")
        print(f"Receita Bruta: {receitaBruta:^42.2f} {receitaBrutaPct:^11.0f}") 
        print(f"Custo Fixo/Administrativo: {custoFixo:11.2f} {custoFixoBD:^48.0f}") 
        print(f"Comissão de Vendas: {comissaoVenda:^31.2f} {comissaoVendaPctBD:^24.0f}") 
        print(f"Imposto: {impostoVenda:^53.2f}{impostoVendaPctBD:.0f}") 
        print(f"Outros Custos: {outrosCustos:^42.2f} {outrosCustosPct:^10.0f}") 
        print(f"Rentabilidade: {rentabilidade:^42.2f} {rentabilidadePct:^10.0f}") 
        print(64 * "=")


        if margemLucroPctBD > 20:
            print("Lucro: Alto")
        elif margemLucroPctBD > 10:
            print('Lucro Médio')    
        elif margemLucroPctBD > 0:
            print("Lucro: Baixo")
        elif margemLucroPctBD < 0:
            print("Lucro: Prejuízo")
        else:
            print("Lucro: Equilíbrio")
        print(64 * "=")
        print('\n')

while True:
    exibir_menu()
        
    opcao = input("Escolha uma opção: ")
        
    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        selecionar_produto()
    elif opcao == "3":
        listar_produto()
    elif opcao == "4":
        deletar_produto()
    elif opcao == "5":
        editar_produto()
    elif opcao == "6":
        break
    else:
        print("\n Opção inválida. Tente novamente. \n ")




