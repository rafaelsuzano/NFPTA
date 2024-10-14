import pandas as pd
import warnings
import matplotlib.pyplot as plt
warnings.simplefilter(action='ignore', category=UserWarning)
warnings.simplefilter(action='ignore', category=FutureWarning)


#
#dataFiles =['dados//2019//ConsultaNFP_33176298862.csv','dados//2020//ConsultaNFP_33176298862.csv','dados//2021//ConsultaNFP_33176298862.csv','dados//2022//ConsultaNFP_33176298862.csv','dados//dados//ConsultaNFP_33176298862 (1).csv']
dataFiles =['dados//dados//ConsultaNFP_33176298862 copy.csv']
df = pd.concat((pd.read_csv(filename, sep='	', encoding='utf-16')for filename in dataFiles ))
#df = pd.read_csv("dados//2020//ConsultaNFP_33176298862.csv", sep='	', encoding='utf-16')
df['CNPJ'] = df['CNPJ emit.'].str.replace('.','').str.replace('/','').str.replace('-','')
df["VALORNF"] = df["Valor NF"].str.replace(',','.').astype(float)
df["ANO"] =  pd.DatetimeIndex(df['Data Emissão']).year
df["MES"] = pd.DatetimeIndex(df['Data Emissão']).month
df["DIA"]  = pd.DatetimeIndex(df['Data Emissão']).day
df["SEMANA"] =  pd.DatetimeIndex(df['Data Emissão']).day_name(locale='pt_BR.utf8')
#print(df)

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
#print(dfSelectCNPJ)



dfSelectEmitente= df.loc[df['Emitente'] == "AMAZON SERVICOS DE VAREJO DO BRASIL LTDA"]
#print(dfSelectEmitente)

#Group by 1
df2 = dfSelectEmitente.groupby('Emitente')['VALORNF'].sum()
#print(df2)


df3 = df.groupby('Emitente')['VALORNF'].sum()
#print(df3)

#Total de Compras Ano
#df4 = df.groupby('ANO')['ANO'].count()


df10 = df.groupby(['ANO','MES'])['MES'].apply(lambda x : x.count()).reset_index(name='Total')
print("rafael")
print(df10)


df9 = df.groupby('ANO')['VALORNF'].apply(lambda x : x.sum()).reset_index(name='Total')
#print(df9)

df4 = df.groupby('ANO')['ANO'].apply(lambda x : x.count()).reset_index(name='Total')
#print(df4)

ano = df4["ANO"].astype(int).astype(str)
total = df4["Total"]
vlr =  df9["Total"]

plt.bar(ano, total)
plt.title('Total de Compras Ano')

plt.xlabel('Ano')
plt.ylabel('Total')

#plt.plot(ano, total, color='green')

#plt.show()






'''

#Total de Compras Ano $
df5 = df.groupby('ANO')['VALORNF'].sum()
print(df5)


#Total de Emitente Ano $
df5 = df.groupby(['Emitente', 'ANO'])['VALORNF'].sum()
print(df5)



#Total de Emitente Ano $

df6 = df.groupby('Emitente')['Emitente'].count()

# Same as SQL having

print(df6)



df7 = df.groupby(['Emitente', 'ANO'])['Emitente'].apply(lambda x : x.count()).reset_index(name='Total')

print(df7)
df8= df7.loc[df7['Total'] > 25]

print(df8)


'''