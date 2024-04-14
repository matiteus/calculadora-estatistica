import get_data as gd
import trabalhar_variaveis as tv
import montar_classes as mc
import analise_estatistica as ae
import export
import math


def main():
    MTC = "media"
    variacao = "baixa"
    dados = gd.importar_dados()
    n,k,h,fi = tv.criar_dados(dados)
    tabela = mc.montar_tabela(dados,k,h,fi)
    med = ae.media(tabela,n)
    moda = ae.moda(tabela,h)
    mediana = ae.mediana(tabela, n,h)
    variancia = ae.variancia(tabela, med, n)
    desvio_padrao = math.sqrt(variancia)
    coef_var = ((desvio_padrao / med) * 100)


    print(f"Media: {med:.2f}")
    print(f"Moda: {moda:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Variancia: {variancia:.2f}")
    print(f"Desvio padrao: {desvio_padrao:.2f}")
    print(f"Coeficiente de variação: {coef_var:.2f}%")
    if coef_var < 15:
        variacao = "baixa"
        MTC = "media"
    elif coef_var < 30:
        variacao = "media"
        MTC = "media"
    elif coef_var < 60:
        variacao = "alta"
        MTC = "mediana"
    else:
        variacao = "alta"
        MTC = "moda"
    print(f"Variacao: {variacao}, usar a {MTC} como medida de tendencia central")
    export.criar_vis_tabela(tabela)

    


if __name__ == "__main__":
    main()