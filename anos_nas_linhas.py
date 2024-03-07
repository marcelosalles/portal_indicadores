### O CÓDIGO PRECISA DE UM ARGUMENTO, PARA DEFINIR O NOME DO OUTPUT

import pandas as pd
import sys

FILENAME = 'C:/Users/704733/Downloads/FloripaNumeros_Indicadores - series ajustando.csv'
ID_VARS = ['id','nome_indicador','label_unidade','tipo_territorial','unidade_territorial','fonte']
COL_NAMES = {
    'id':'Série ID',
    'nome_indicador':'Nome Série',
    'tipo_territorial':'Tipo Territorial',
    'unidade_territorial':'Unidade Territorial',
    'label_unidade':'Unidade do Dado',
    'fonte':'Fonte'
}

name = sys.argv[1]

df = pd.read_csv(FILENAME, encoding='utf-8')
df = df.drop('serie',axis=1)

df = pd.melt(df, id_vars=ID_VARS, var_name="Ano", value_name="Valor")

df = df[df['Valor'].notna()]

df.tipo_territorial = df.tipo_territorial.replace('Município','MUNICIPALITY')
df.tipo_territorial = df.tipo_territorial.replace('Município','DISTRICT')

df = df.rename(columns=COL_NAMES)

df.to_csv(f'series_{name}.csv',index=False)
