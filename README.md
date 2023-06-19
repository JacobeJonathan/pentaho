# pentaho
pentahopractico
## Regular expresion para extraer varios archivos excel csv
1.-text file input
2.- table output
datos_[0-9].csv
## leer multiples archivos excel xlsx
- elegimos : microsoft excel input
- Luego tenemos que crear la formula para todo esos archivos
- https://regexr.com/
- dentro del enlace anterior creamos la formula pero primeo lo copiamos
- HS_[A-Z-0-9]*_[0-9]*_[0-9]*.xlsx
- y es nuestra formula que tomara todos los archivos
- cambiamos a xlxs
- copiamos el directorio donde se encuentran los archivos
- y le damos en add 
- comprovamos si se agregaron correctamente dando clic en show filename
### como hacer para que reconozca todas las hojas
- damos click en microsoft excel input
- nos vamos a sheets
- damos clic en get sheetname
- y os reconoce
- y agregamos todas es decir pasamos de izqueida a derecha
### eliminar columnas
- eliminamos porque se duplican y hay muchas y solo deben coincidir con la columnas de la base de datos
- nos vamos a fields 
- get fields
- vemos la estructura de los archivos excel
- damos clic desde donde no empiza
- nos vamos al ultimos y damo shft y clic
- luego clic izquierod y elimmar lines
## extraer informacion desde un zip
1. Primero abrimos buscamos donde esta el archivo zip
2. le damos en add ( agreagamos el enlace o la direccion donde se encuentra el archivo)
3. buscmaos n text file input y lo abrimos
4. nos vamos a content 
5. cambiamos el separador a una coma ,
6. cambiamos la compresion a zip
7. cambiamos el format a mixed
8. nos vamos a fields y ponemos los filas
9. y le damos preview rows
## extraer infromacion desde un xml
- buscamos el archivo get data from XML
- buscamos donde esta el archivo xml
- le damos en add
- ponemos en loopxpath (/dataset/record)
- nos vamos a fields 
- get fields
- previews fields
- y ok
## extraer informacion desde un json
- buscamos en json input
- buscamos donde esta el archivo json
- luego nos vamos a fields
## realizar un etl ejemplo practico
- buscamos donde esta el archivo csv
- buscamos en pentaho el archivo csv file input
- cambiamos el delimitador por input
- le datos en get files
- luego en preview
### cambiamos un fila "rows"
- buscamos en pentaho select values
- csv file input lo conectamos con select values
- get fields to selectd
- cambiamos el row sexo a genero
- en select values el fieldname ponemos sexo y en rename to genero_id
- selccionamos todo y run
### cambiar destro de los rows
- cambiar de male y famele a 1 y 2
- buscamos en pentaho replace in string
- luego conectamos select values con replace string
- abrimos
- in strinf field ponemos el campo genero_id
- search Male
- Replace with le damos el valor de 1
- y en whole word le damos en Y o yes
- y ok
- y de igual manera par female y non-bnary
### CAMBIAR EL NOMBRE EN TODO MAYUSCULA
- buscmos string operation
- lo unimos o enlazamos con replace in string
- abrimos
- in stream fields nombre
- lower/upper ponemos upper
- en remove special character carriage return
- ok
### HACER QUE EL CAMPO ID SIEMPRE SEA UNICO NO DUPLICAODS
- buscmaos en pentaho unique rows
- lo unimos con el anterior
- fieldname id
- ignore case le damos en yes o y
- ok
### cambio de tipo de dato varchar a integer
- esro hacemos porque la base de datos esta con integer y en el etl esta con varchar
- esccogemos en pentaho select values
- entramos
- fieldname genero_id
- type integer
- ok
### subir todo el etl a la base de datos
- table output
- nos conectamos a la base de datos sql server
- podemosen target schema dbo
- target table personas
- commit size 100
- spexify databases tables check
- nos vamos a databases fields
- get fields
- ejecutamos todo y observamos en la base de datos sqlserver
- ![Visualizacio ](/src/todoetl.jpg)
## filtrando rows (filas) y exportar a otro csv
- primero eescogemos importamos el  archivo csv a pentaho
- luego enlazamos
- a split fields
- separamos es decir si tenemos
- jonathanjacob@gmail.com
- agregamos 2 campos
- campo_1
- campo_2
- lo serpara en dos
- jonathanjacob
- gmail.com
- y asi podemos separar en mas rows
- podemos exportar con microsft excel output
## sacando los valores unicos y unirlos para que no aya registros repetidos
- quitamos los duplicados y los unimos en uno solo
## añadimos id
- añadimos id con add sequence
- luego agregamos en select values para ordenar de id hasta telefono
## ejemplo practico calculator
- solo ponemos calculator en spoon
- agregamos una nueva fila
- calculator

## CREANDO SCRIPT CON PYTHON Y PENTAHO
- abrimos visual studio code en la carpeta de los archivos excel
  ´´´py
      import os
    import pandas as pd
    ditectorio = r"C:\Users\jonat\Downloads\trabajopentaho\leermultiplosarchivosCSV"
    arr = os.listdir(ditectorio)
    archivos = []
    for i in arr:
        if '.csv' in i:
            archivos.append(i)
        dfs = []
    for i in archivos:
        ar = ditectorio + f"\{i}"
        df_temp = pd.read_csv(ar)
        dfs.append(df_temp)
    
    result = pd.concat(dfs)
    print(result)
  
  ´´´
- ejecutamos con python main.py
- ![datos ](/src/2.png)
