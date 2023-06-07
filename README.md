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

