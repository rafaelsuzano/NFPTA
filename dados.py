import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)
warnings.simplefilter(action='ignore', category=FutureWarning)

df = pd.read_csv("dados//2020//ConsultaNFP_33176298862.csv", sep='	', encoding='utf-16')
df['CNPJ'] = df['CNPJ emit.'].str.replace('.','').str.replace('/','').str.replace('-','')
df["VALORNF"] = df["Valor NF"].str.replace(',','.').astype(float)
df["ANO"] =  pd.DatetimeIndex(df['Data Emissão']).year
df["MES"] = pd.DatetimeIndex(df['Data Emissão']).month
df["DIA"]  = pd.DatetimeIndex(df['Data Emissão']).day
df["SEMANA"] =  pd.DatetimeIndex(df['Data Emissão']).day_name(locale='pt_BR.utf8')
print(df)

## Group by Ano Conta
dfAnoConta = df.groupby('ANO')['ANO'].count()
#print(dfAnoConta)


## Group by Ano Soma
dfAnoSoma = df.groupby('ANO')['ANO'].sum()
#print(dfAnoSoma)

## Group by Mes Conta
dfMesConta = df.groupby('MES')['MES'].count()
#print(dfMesConta)


## Group by Mes Soma
dfMesSoma = df.groupby('MES')['VALORNF'].sum()
#print(dfMesSoma)



#Select empresa
dfSelectEmitente= df.loc[df['Emitente'] == "AMAZON SERVICOS DE VAREJO DO BRASIL LTDA"]
#print(dfSelectEmitente)



#Select cnpjsenhase
dfSelectCNPJ= df.loc[df['CNPJ emit.'] == "47.508.411/1665-50"]
print(dfSelectCNPJ)



dfSelectEmitente= df.loc[df['Emitente'] == "AMAZON SERVICOS DE VAREJO DO BRASIL LTDA"]
#print(dfSelectEmitente)

#Group by 1
df2 = dfSelectEmitente.groupby('Emitente')['VALORNF'].sum()
print(df2)


df3 = df.groupby('Emitente')['VALORNF'].sum()
print(df3)


