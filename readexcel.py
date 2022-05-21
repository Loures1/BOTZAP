import pandas as pd
from pathlib import Path

def Planilha():
    path = Path('planilha_excel')
    arquivos_xlsx = list(path.glob('*.xlsx'))

    if len(arquivos_xlsx) == 1:
        return arquivos_xlsx[0]
    else: 
        return None

def Contatos():
    arquivo_planilha = Planilha()
    if arquivo_planilha != None:
        pd_planilha = pd.read_excel(arquivo_planilha)
        contatos = pd_planilha['Unnamed: 2'][1:]
        return list(contatos)
    else:
        print('ERROR: MAIS DE UM ARQUIVO EXCEL NA PASTA')
        


