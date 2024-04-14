import pandas as pd

def importar_dados():
    #pegar os dados da planilha excel
    dados = pd.read_excel('data.xlsx')
    #converter a dadosframe para um array simples
    dados_array = dados.values.flatten()
    return(dados_array)

