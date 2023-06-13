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


