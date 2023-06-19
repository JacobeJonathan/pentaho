import os #importamos os
import pandas as pd # importamos pandas
ditectorio = r"C:\Users\jonat\Downloads\trabajopentaho\leermultiplosarchivosCSV" #ruta donde se encuentran los archivos
arr = os.listdir(ditectorio) #lista de archivos en el directorio
archivos = [] #lista vacia
for i in arr:
    if '.csv' in i:
        archivos.append(i)
    dfs = []
for i in archivos:
    ar = ditectorio + f"\{i}"
    df_temp = pd.read_csv(ar)
    dfs.append(df_temp)

result = pd.concat(dfs) #concatenamos los archivos

result_csv = "C:/Users/jonat/Downloads/trabajopentaho/leermultiplosarchivosCSV/result.csv" #ruta donde se guardara el archivos
result.to_csv(result_csv, index=False)

print(result)