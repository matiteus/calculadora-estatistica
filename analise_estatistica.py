
def media(tabela,n):
    med = 0
    for i in range(1,len(tabela)-1):
        med += (tabela[i][3]*tabela[i][4])
    med/=n
    return med

def moda(tabela,h):
    #encontrar o mais repetido
    repetido = tabela[1][3]
    pos_repetido = 1
    for i in range(2,len(tabela)-1):
        if tabela[i][3] > repetido:
            repetido = tabela[i][3]
            pos_repetido = i
    fi_modal = tabela[pos_repetido][3]
    limite_inf_classe_modal = tabela[pos_repetido][0]
    #encontrar D1
    if pos_repetido == 1:
        d1 = fi_modal
    else:
        d1 = tabela[pos_repetido][3]-tabela[pos_repetido-1][3]
    #encontrar D2
    if pos_repetido == len(tabela)-1:
        d2 = fi_modal
    else:
        d2 = tabela[pos_repetido][3]-tabela[pos_repetido+1][3]
    
    moda = limite_inf_classe_modal+((d1/(d1+d2))*h)
    return moda

def mediana(tabela, n,h):
    #verificar o total de dados é par ou impar
    medpar = n & 1 == 0
    #ver qual a posição a se buscar
    if medpar:
        posmediana = n/2
    else:
        posmediana = (n+1)/2
    # buscar a linha da mediana
    for i in range(1, len(tabela)-1):
        if tabela[i][5] <=  posmediana <= tabela[i+1][5]:
            break
    i+=1
    #calculo da mediana
    mediana = tabela[i][0] + (((posmediana-tabela[i-1][5])*h)/tabela[i][3])
    return mediana

def variancia(tabela,media, n):
    
    somatorio = 0
    for i in range(1, len(tabela)-1):
        fi_x2 = tabela[i][3]*(tabela[i][4]*tabela[i][4])
        somatorio += fi_x2
    somatorio/=n
    somatorio -= media*media
    n = (n/(n-1))
    var = somatorio*n
    return var
