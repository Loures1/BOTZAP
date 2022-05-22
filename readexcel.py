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

def Grupos():
    with open('config/grupos.txt', 'r', encoding='utf8') as arquivo:
        grupos = []
        linhas = arquivo.readlines()
        for linha in linhas:
            grupos.append(linha.replace('\n', ''))
    return(grupos)

def Mensagem():
    with open('config/mensagem.txt', 'r', encoding='utf8') as arquivo:
        mensagens = {'mensagem': '',
                    'mensagem-grupo': ''}
        linhas = arquivo.readlines()
        for linha in linhas:
            caracteres = ['Mensagem:', 'Mensagem-grupo:', '\n']
            if 'Mensagem:' in linha:
                mensagens['mensagem'] = linha
                for caractere in caracteres:
                    mensagens['mensagem'] = mensagens['mensagem'].replace(caractere, '')
            
            if 'Mensagem-grupo:' in linha:
                mensagens['mensagem-grupo'] = linha
                for caractere in caracteres:
                    mensagens['mensagem-grupo'] = mensagens['mensagem-grupo'].replace(caractere, '')
        
    return mensagens

Grupos()