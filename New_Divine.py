# Bloco 1 ------------------------------------------------------------------------------------------------------------------------------------

p = '======================================================================================'
import os
import time
from Givining_UP import estoques, compras, ganhos, precos, calculos, desconto
import re
from datetime import datetime, timedelta

def relatorio_compras(periodo):
    agora = datetime.now()
    compras_filtradas = []

    # Define o intervalo de tempo com base no período
    if periodo == "dia":
        inicio = agora.replace(hour=0, minute=0, second=0, microsecond=0)
        fim = inicio + timedelta(days=1)
        periodo_str = "hoje"
    elif periodo == "semana":
        inicio = agora - timedelta(days=agora.weekday())
        inicio = inicio.replace(hour=0, minute=0, second=0, microsecond=0)
        fim = inicio + timedelta(weeks=1)
        periodo_str = "esta semana"
    elif periodo == "mes":
        inicio = agora.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        fim = (inicio + timedelta(days=32)).replace(day=1)
        periodo_str = "este mês"
    elif periodo == "ano":
        inicio = agora.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        fim = inicio.replace(year=inicio.year + 1)
        periodo_str = "este ano"
    else:
        print("Período inválido.")
        return

    # Lê os dados do arquivo Banco_de_Dados.txt
    with open('Banco_de_Dados.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    # Filtra as compras dentro do período
    for linha in linhas:
        try:
            # Divide a linha em partes com base no formato esperado
            partes = linha.split(", ")
            valor_compra_str = partes[1].split(":")[1].strip()  # Extrai o valor da compra
            data_str = partes[2].replace("Data: ", "").strip()  # Extrai a data da compra

            # Converte os valores para os tipos corretos
            valor_compra = float(valor_compra_str.split()[0])  # Remove "peças" e converte para float
            data_compra = datetime.strptime(data_str, '%d/%m/%Y %H:%M:%S')  # Converte a data para datetime

            # Verifica se a data está dentro do intervalo
            if inicio <= data_compra < fim:
                compras_filtradas.append({"data_compra": data_compra, "valor_compra": valor_compra})
        except Exception as e:
            print(f"Erro ao processar linha: {linha}. Erro: {e}")

# Bloco 1 ------------------------------------------------------------------------------------------------------------------------------------        
# Bloco 2 ------------------------------------------------------------------------------------------------------------------------------------
    # Exibe o relatório
    print(p)
    print(f"\n--- Relatório de Compras {periodo_str.capitalize()} ---")
    print(f"Total de compras: {len(compras_filtradas)}")
    for compra in compras_filtradas:
        print(f"Valor: R$ {compra['valor_compra']:.2f} - Data: {compra['data_compra'].strftime('%d/%m/%Y %H:%M:%S')}")
    print(p)
    time.sleep(5)
    os.system('cls')
# Bloco 2 ------------------------------------------------------------------------------------------------------------------------------------
while True: 
    os.system("cls")
    print(p)
    print('Seja muito bem vindo ao serviços de auto peça')
    print('qual seu objetivo por hj ?')
    print(p)
    time.sleep(4)
    os.system("cls")
    print(p)
    escolhas = int(input(
        "Escolha uma das opções abaixo:\n"
        "1 - Abrir a parte de funcionários\n"
        "2 - Realizar uma compra de peças\n"
        "Digite sua escolha: "
    ))
    print(p)
    time.sleep(1)
    os.system('cls')
    print(p)
    print('Verificando .......')
    print(p)
    time.sleep(1)
    os.system("cls")
    # Bloco 2 ------------------------------------------------------------------------------------------------------------------------------------
    # Bloco 3 ------------------------------------------------------------------------------------------------------------------------------------
    if escolhas == 1:
        print(p)
        print('Seja muito bem vindo a parte de funcionários')
        print(p)
        time.sleep(2)
        with open('Banco_de_Dados.txt', 'r') as arquivo:
            conteudo = arquivo.readlines()
        
        print(p)
        print('Dados do arquivo:')
        for linha in conteudo:
            print(linha.strip()) 
        print(p)

        with open('EstMax.txt', 'r') as arquivo:
            estvol = int(arquivo.readline().strip())
        
        with open('Estoques.txt', 'r') as arquivo:
            estoque_atual = int(arquivo.readline().strip())

        
        CE=  estoque_atual


        estvol1 = (estvol - CE)

        print(p)
        print(f'Estoque Atuais:{estvol1}')
        print(p)

        print('O que deseja fazer ?')
        print(p)
        time.sleep(2)
        escolhas2 = int(input(
            "Escolha uma das opções abaixo:\n"
            "1 - alterar dados 1\n"
            "2 - inserir dados 2 \n"
            '3 - deletar dados 3\n'
            '4 - mostrar vendas do total no estoque 4\n'
            '5 - relatorio de vendas dia-semana-mes-ano 5\n'
            "Digite sua escolha: "
        ))
        # Bloco 3.1 ------------------------------------------------------------------------------------------------------------------------------------
        if escolhas2 == 1:
            time.sleep(2)
            os.system('cls')
            print(p)
            print('Alterando dados .......')
            print(p)
            time.sleep(2)
            os.system('cls')
            with open('EstMax.txt', 'w') as arquivo:
                arquivo.write('')

            alter = int(input('Digite a quantidade de peças que deseja que tenha no estoque maximo agr: '))

            with open('EstMax.txt', 'w') as arquivo:
                arquivo.write(f'{alter}')
            
            time.sleep(2)
            os.system('cls')
            print(p)
            print('Alterando dados .......')
            print(p)

            print(p)
            print('Dados alterados com sucesso')
            print(p)
            time.sleep(2)
            os.system('cls')
    # Bloco 3.2 ------------------------------------------------------------------------------------------------------------------------------------
        elif escolhas2 == 2:
            
            with open('EstMax.txt', 'r') as arquivo:
                estins = int(arquivo.readline().strip())
            
            print(p)
            ins= int(input('Digite a quantidade de peças que deseja inserir no estoque: '))
            print(p)
            time.sleep(2)
            os.system('cls')

            with open('EstMax.txt', 'w') as arquivo:
                arquivo.write(f'{estins + ins}')

            
            print(p)
            print('Inserindo dados .......')
            print(p)
            time.sleep(2)
            os.system('cls')

            print(p)
            print('Dados inseridos com sucesso')
            print(p)

            time.sleep(2)
            os.system('cls')
    # Bloco 3.3 ------------------------------------------------------------------------------------------------------------------------------------
        elif escolhas2 == 4:
            print(p)
            time.sleep(2)
            with open('EstMax.txt', 'r') as arquivo:
                estomax = int(arquivo.readline().strip())

            with open('Estoques.txt', 'r') as arquivo:
                estoque_atual = int(arquivo.readline().strip())

            
            Por = (estoque_atual /estomax ) * 100
            
            print(p)
            print(f'Vendas a partir do estoque total:{Por} %')
            print(p)
            time.sleep(5)
            os.system('cls')
    # Bloco 3.4 ------------------------------------------------------------------------------------------------------------------------------------
        elif escolhas2 == 5:
            print(p)
            print("Escolha o período para o relatório:")
            print("1. Dia")
            print("2. Semana")
            print("3. Mês")
            print("4. Ano")
            periodo_opcao = input("Digite sua escolha: ")
            print(p)
            time.sleep(3)
            os.system('cls')

            if periodo_opcao == "1":
                relatorio_compras("dia")
            elif periodo_opcao == "2":
                relatorio_compras("semana")
            elif periodo_opcao == "3":
                relatorio_compras("mes")
            elif periodo_opcao == "4":
                relatorio_compras("ano")
            else:
                print("Opção inválida.")

    # Bloco 3.5 ------------------------------------------------------------------------------------------------------------------------------------     
        else:
            
            print(p)
            print('Deletando dados .......')
            print(p)
        
            with open('Banco_de_Dados.txt', 'w') as arquivo:
                arquivo.write('')

            with open('Estoques.txt', 'w') as arquivo:
                arquivo.write('0')

            time.sleep(2)
            os.system('cls')
            print(p)
            print('Dados deletados com sucesso')
            print(p)
            time.sleep(2)
            os.system('cls')

    # Bloco 3.5 ------------------------------------------------------------------------------------------------------------------------------------
    # Bloco (continuação bloco 3) ------------------------------------------------------------------------------------------------------------------------------------
    else:
        print(p)
        print('Seja muito bem vindo a parte de compras')
        print(p)
        time.sleep(2)
        os.system('cls')
        print(p)
        print('Quantas peças deseja comprar, cada peça custa 10 reais e tem um deconto de 5% ?')
        print(p)
        compra = int(input('Digite a quantidade de peças que deseja comprar: '))
        print(p)
        time.sleep(2)

        import Givining_UP
        Givining_UP.compras += compra

        print(p)
        time.sleep(2)
        os.system('cls')
        print(p)
        print('Calculando .......')
        print(p)
        time.sleep(2)
        os.system('cls')
        
        calculos = Givining_UP.compras * precos
        desconto = calculos * 0.05
        valordescontos = calculos - desconto

        print(p)
        print(f'a sua compra foi de {calculos} reais')
        print(p)
        time.sleep(1)
        print(p)
        print(f'Porem com o desconto de primeira compra de 5% fica no valor de {valordescontos} reais')
        print(p)
        
        with open('Estoques.txt', 'r') as arquivo:
            estoque_atual = int(arquivo.readline().strip())

        
        CE=  estoque_atual + compra
        
        with open('Estoques.txt', 'w') as arquivo:
            arquivo.write(f'{CE}')

        data_atual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        with open('Banco_de_Dados.txt', 'a') as arquivo:  
            arquivo.write(f'Compra: {Givining_UP.compras} peças, Total: {calculos} reais, Data: {data_atual}\n')
        
        print('Os dados da compra foram salvos no arquivo "Banco_de_Dados.txt".')
        print(p)
        time.sleep(4)
        os.system('cls')
    # Bloco 3 Fim ------------------------------------------------------------------------------------------------------------------------------------