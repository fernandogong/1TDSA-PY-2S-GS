# Fernando Gong     RM:93823
# Jefferson Lemos   RM:95208
# Lucas Sabonaro    RM:95518

##### SUBALGORITMOS #####
#ler o input e conferir se é int
def leiaInt(msg):
    while True:
        opcao = str(input(msg))
        if opcao.isnumeric():
            valor = int(opcao)
            break
        else:
            print()
            print('\033[0;31mERRO! Digite uma opção valida.\033[m')
            print()
    return valor

#ler o input e conferir se é string
def leiaStr(msg):
    while True:
        opcao = str(input(msg))
        if opcao.isnumeric() == False:
            valor = str(opcao)
            break
        else:
            print()
            print('\033[0;31mERRO! Digite uma opção valida.\033[m')
            print()
    return valor

#menu principal
def menu_principal():
    print()
    print('0 - ENCERRAR PROGRAMA')
    print('1 - Cadastrar mes de referencia')
    print('2 - Exibir dados do mes de referencia[pesquisa por mes]')
    print('3 - Relatorio comparativo[referencia 2019]')
    print('4 - Listar todos os meses cadastrados')
    print()

#cadastra o mes-ano, total de habitantes e total de obitos
def cadastrarMesAno(cma, c):
    print('*-' * 30)
    print("CADASTRANDO MES-ANO DE REFERENCIA")
    print()
    continuar = 's'
    while True:
        if continuar == 's':
            cma['mes_ano'] = leiaStr("Mes-ano(mm-aaaa)........:")
            cma['total_habitantes'] = leiaInt("Total de Habitantes.....:")
            cma['total_obitos'] = leiaInt("Total de obitos.........:")
            print()
            c.append(cma.copy())
            print("***** GRAVADO COM SUCESSO *****")
            continuar = leiaStr("Digite (S)im para continuar cadastrando"
                                " ou (N)ao para voltar ao menu: ").lower()
        elif continuar == 'n':
            break
        else:
            print("Opcao invalida!")
    print('*-' * 30)

#exibe as informacoes do mes-ano digitado
def consultarMesAno(c):
    print('*-' * 30)
    print("CONSULTANDO MES-ANO DE REFERENCIA")
    print()
    consulta = leiaStr("Digite o mes-ano desejado(mm-aaaa): ")
    print()
    if len(c) >= 1:
        for i in range(0, len(c)):
            if c[i]['mes_ano'] == consulta:
                print()
                print(f"Mes-ano(mm-aaaa)........: {c[i]['mes_ano']}")
                print(f"Total de Habitantes.....: {c[i]['total_habitantes']}")
                print(f"Total de obitos.........: {c[i]['total_obitos']}")
                print()
                print("***** REGISTRO ENCONTRADO *****")
    else:
        print("***** MES-ANO NAO CADASTRADO *****")
    print('*-' * 30)

#exibe as informacoes do ano digitado
def compararRelatorio(c):
    print('*-'*30)
    print("RELATORIO COMPARATIVO DE TAXA DE MORTALIDADE ANUAL")
    print()
    soma_hab, soma_obito = 0, 0
    ano = int
    comparar = leiaInt("Digite o ano a ser comparado(aaaa): ")
    print()
    if len(c) >= 1:
        for i in range(0, len(c)):
            a = c[i]['mes_ano'].rsplit('-', 1)
            ano = a[1]
            if int(a[1]) == comparar:
                for j in range(1, len(a)):
                    soma_hab += c[i]['total_habitantes']
                    soma_obito += c[i]['total_obitos']
        comp = (soma_obito / soma_hab) * 100000
        print()
        print(f"Total de Habitantes......................: {soma_hab}")
        print(f"Total de obitos..........................: {soma_obito}")
        print(f"Total de mortes por 100k habitantes(2021): {comp:.2f}")
        print(f"Total de mortes por 100k habitantes(2019): {15:.2f}")
        print(f"Comparativo % entre {ano}-2019: {(comp-15)*100/15:.1f}%")

        print()
        print("Sendo:")
        print()
        #abaixo há a explicacao de cada item acima
        print('"Total de habitantes": a somatoria de todos os habitantes cadastrados'
              ' nos meses do ano escolhido.')
        print('“Total de óbitos”: a somatória de todos os óbitos cadastrados nos meses'
              ' do ano escolhido.')
        print(f'“Taxa por 100k habitantes – {ano}”: É o cálculo envolvendo'
              ' as duas somatórias acima do ano referido.')
        print('“Taxa por 100k habitantes – 2019”: É o dado que o texto forneceu')
        print(f'“Comparativo % entre {ano}-2019”: É o comparativo da proporção'
              ' das duas últimas taxas.')
    else:
        print("***** NENHUM CADASTRO FOI ENCONTRADO *****")
    print('*-' * 30)

#lista todos os registros cadastrados
def listarTodosCadastros(c):
    print('*-' * 30)
    if len(c) >= 1:
        for i in range(0, len(c)):
            print()
            print(f"Mes-ano(mm-aaaa)........: {c[i]['mes_ano']}")
            print(f"Total de Habitantes.....: {c[i]['total_habitantes']}")
            print(f"Total de obitos.........: {c[i]['total_obitos']}")
            print()
        print("***** REGISTROS ENCONTRADOS *****")
    else:
        print("***** NENHUM CADASTRO FOI ENCONTRADO *****")
    print('*-' * 30)

### VARIAVEIS ###
cadastro_mes_ano = {}
clone = []

##### PROGRAMA PRINCIPAL #####
while True:
    menu_principal()
    opcao = leiaInt("Digite a opcao desejada: ")
    print()
    if opcao == 0:
        print("PROGRAMA ENCERRADO!")
        break
    else:
        if opcao == 1:
            cadastrarMesAno(cadastro_mes_ano, clone)
        elif opcao == 2:
            consultarMesAno(clone)
        elif opcao == 3:
            compararRelatorio(clone)
        elif opcao == 4:
            listarTodosCadastros(clone)