import math
import numpy as np

def criar_dados(dados):
    #conseguir a amplitude total
    #guardando em uma variavel separada para ser usado na montagem da classe
    primeiro_dado=dados.min()
    at = abs(primeiro_dado - dados.max())
    #conseguir o numero de dados na tabela (seria mais eficiente usar len(dados) no lugar da variavel, mas para transparencia será definida uma variavel)
    n = len(dados)
    #conseguir o valor de K
    if n <= 25:
        k = 5
    else:
        #k deve ser arredondado para cima em caso de número real
        k = math.ceil(math.sqrt(n))
    #encontrar a amplitude de cada classe
    h = math.ceil(at/k)
    #definindo a primeira classe
    primeiro_dado = math.floor(primeiro_dado)
    #definindo o array de fi
    fi = np.zeros(k,dtype = int)
    j=0
    #gerando as classes
    for i in range(n):
        if primeiro_dado <= dados[i] < primeiro_dado+h:
            fi[j] += 1
        else:   
            j +=1
            fi[j] += 1
            primeiro_dado += h
        
    return (n,k,h, fi)


