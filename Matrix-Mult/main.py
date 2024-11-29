import fc 
from time import sleep

print('MULTIPLICAÇÃO DE MATRIZES\n')
sleep(1/2)

while True:
    print('MATRIZ 1: \n')
    
    while True:
        try: 
            linhas_matriz = int(input('Número de linhas da sua matriz 1: '))
            colunas_matriz = int(input('Número de colunas da sua matriz 1: '))
        
        except:
            print('Você deve inserir apenas valores numéricos.\n')
        
        else:
            break

    
    matriz1, certo = fc.matriz(linhas_matriz,colunas_matriz)
    if certo == False:
        print(f'\nSua matriz {colunas_matriz} x {linhas_matriz} deveria conter {colunas_matriz*linhas_matriz} elemento(s),', end='')
        print(f' porém contém {sum(len(sublista) for sublista in matriz1)} elemento(s).')
        print(f'Insira sua matriz novamente.\n')
        continue

    fc.mostrar(matriz1,'MATRIZ 1')


    while True:
        voltar = fc.voltar('Inserir a segunda matriz')
        if voltar == 2: break
        elif voltar == 3: 
            voltar = 4
            break
    
        
        while True:
            voltar = 1
            print('')
            print('MATRIZ 2: \n')
            
            while True:
                try: 
                    linhas_matriz = int(input('Número de linhas da sua matriz 2: '))
                    colunas_matriz = int(input('Número de colunas da sua matriz 2: '))
                
                except:
                    print('Você deve inserir apenas valores numéricos.\n')
                
                else:
                    if len(matriz1[0]) != linhas_matriz:
                        print('Essas matrizes não podem ser multiplicadas, pois o número de colunas da matriz 1 é diferente do número de linhas da matriz 2')
                        voltar = fc.voltar('Voltar - Inserir a Matriz 2','Voltar - Inserir a Matriz 1')
                        if voltar == 2 or voltar == 3:
                            break
                    else: break
                
            if voltar == 3: 
                voltar = 4
                break
            if voltar == 2: break
        
        

            matriz2, certo = fc.matriz(linhas_matriz,colunas_matriz)

            if certo == False:
                    print(f'\nSua matriz {colunas_matriz} x {linhas_matriz} deveria conter {colunas_matriz*linhas_matriz} elemento(s),', end='')
                    print(f' porém contém {sum(len(sublista) for sublista in matriz2)} elemento(s).')
                    print(f'Insira sua matriz novamente.\n')
                    continue

            fc.mostrar(matriz2,'MATRIZ 2')

            voltar = fc.voltar('Multiplicar as matrizes','Voltar - Inserir a matriz 2','Voltar - Inserir a matriz 1')
            if voltar == 2: continue
            elif voltar == 3:
                voltar = 2
                break
            elif voltar == 4: break
            

            
            resultante = fc.multiplicar(matriz1,matriz2)

            fc.mostrar(resultante,'MATRIZ RESULTANTE')

        if voltar == 2: break

    if voltar == 2: continue
    if voltar == 4: break
    




    

    