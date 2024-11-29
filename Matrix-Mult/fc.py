from time import sleep

def matriz(linhas,colunas):
    
    print('')
    matriz = []
    for i in range(linhas):
        while True:
            try:
                linha = input(f'Digite as entradas da {i+1}° linha: ').split()
                for ii in range(len(linha)):
                    linha[ii] = int(linha[ii])
                matriz.append(linha)
            except:
                print('Você deve inserir apenas valores numéricos válidos.\n')
                continue
            else: 
                break

    return matriz, True if sum(len(sublista) for sublista in matriz) == colunas*linhas else False 


def multiplicar(matriz1,matriz2):
    resultante = []
    linha_resultante = []
   
    for i,linha in enumerate(matriz1):
        linha_resultante.clear()

        for ii in range(len(matriz2[0])):
            elemento = 0
            for iii in range(len(matriz2)):
                elemento += linha[iii]*matriz2[iii][ii]

            linha_resultante.append(elemento)
        
        resultante.append(linha_resultante[:])

    return resultante


def mostrar(matriz,txt):
    sleep(1/2)
    print(f'\n{txt}: ')
    sleep(1/2)
    print('')
    for i in matriz:
        print(' '*17, end='')
        for ii in i:
            print(f'{ii: <6}', end='')
        print('')
    sleep(1/2)
                

def voltar(txt,voltar1='',voltar2=''):

    if voltar1 != '' and voltar2 == '':
        print(f'\n[1] - {txt}')
        print(f'[2] - {voltar1}')
        print('[3] - Sair')

    elif voltar1 != '' and voltar2 != '':
        print(f'\n[1] - {txt}')
        print(f'[2] - {voltar1}')
        print(f'[3] - {voltar2}')
        print('[4] - Sair')

    else:
        print(f'\n[1] - {txt}')
        print('[2] - Voltar')
        print('[3] - Sair')

    while True:
        try:
            option = int(input('\nDigite a opção desejada: '))
            options = [1,2,3]
            if option in options:
                break
            else:
                print('Você deve digitar apenas valores válidos [1] - [2] - [3]')
        except:
            print('Você deve digitar apenas valores válidos [1] - [2] - [3]')

    return option