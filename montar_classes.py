import math

def montar_tabela(dados,k,h,fi):
    primeiro_dado = math.floor(dados.min())
    #declaração da tabela
    tabela = [["" for _ in range(7)] for _ in range(k+2)]

    #criação dos rotulos
    tabela[0][0] = "Classes"
    tabela[0][1] = ""
    tabela[0][2] = ""
    tabela[0][3] = "fi"
    tabela[0][4] = "xi"
    tabela[0][5] = "fa"
    tabela[0][6] = "fa%"
    tabela[k+1][0] = "Total"

    somafi=0
    #montagem da tabela
    for i in range(1,k+1):
        tabela[i][0] = primeiro_dado
        tabela[i][1] = "⊢"
        tabela[i][2] = primeiro_dado+h
        
        tabela[i][3] = fi[i-1]
        somafi+=fi[i-1]
        tabela[i][4] = (primeiro_dado+h + primeiro_dado)/2
        primeiro_dado += h
        tabela[i][5] = somafi
        tabela[i][6] = (tabela[i][5]/len(dados))*100
    tabela[8][3] = somafi
    tabela[8][6] = (somafi/len(dados))*100
    for i in range(1,k+1):
        tabela[i][6] = f"{tabela[i][6]:.2f}%"
    return tabela
