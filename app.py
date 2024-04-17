import pandas as pd

# lee el archivo csv
data_frame = pd.read_csv('datos.csv')

# print(data_frame)

# muestra los primeros valores de la columna x
# print(data_frame.head('x'))

# realiza automanticamente la Frecuencia Absoluta Acumulada (Fi)
data_frame['Fi'] = data_frame['fi'].cumsum()

# realiza automanticamente la Frecuencia Relativa Simple (ri)
data_frame['ri'] = (data_frame['fi'] / data_frame['fi'].sum()).round(4)

# realiza automanticamente la Frecuencia Relativa Acumulada (Ri)
data_frame['Ri'] = data_frame['ri'].cumsum()

# realiza automanticamente la Frecuencia Porcentual simple (pi)
data_frame['pi%'] = (data_frame['ri'] * 100).round(2)

# realiza automanticamente la Frecuencia Porcentual Acumulada (Pi)
data_frame['Pi%'] = (data_frame['Ri'] * 100).round(2)


print(data_frame)

# guarda el archivo en el portapapeles
data_frame.to_clipboard(index= False)