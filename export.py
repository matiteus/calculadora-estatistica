import pandas as pd


def criar_vis_tabela(tabela):
    df = pd.DataFrame(tabela)
    df.to_excel('tabela.xlsx')

        

        