import pandas as pd
#https://pypi.org/project/cnpj-py/
from cnpj import CNPJClient
from pprint import pprint



import csv
import pandas as pd
df = pd.read_csv('tudo.csv',  sep='\t',encoding='UTF-16', quoting=csv.QUOTE_NONE, on_bad_lines='skip')
#


#for col in df.columns:
 # print(col)





#print(df['"Situação do Crédito"'].to_string())

#print(df['"Situação do Crédito"'].drop_duplicates().str.replace('"', '').to_string(index=False,header=False))

#print(df['"CNPJ emit."'].drop_duplicates().str.replace('"', '').str.replace('.', '').str.replace('/', '').str.replace('-', '').to_string(index=False,header=False))
#cnpj_client = CNPJClient()
#resultado = cnpj_client.cnpj('11857685000103')

#pprint(resultado['endereco'])

#pprint(resultado)
x=(df['"CNPJ emit."'].str.replace('"', '').str.replace('.', '').str.replace('/', '').str.replace('-', '').to_string(index=False,header=False))


df2 = x.groupby('"CNPJ emit."').count()


print(df2)