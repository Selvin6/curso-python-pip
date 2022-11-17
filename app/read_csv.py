import csv

#Para leer cada fila se crea la función, pero se muestra una lista, y no es lo más facil de utilizar
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    #Nombre de las columnas
    header = next(reader)
    #Retornar una lista con todos los diccionarios
    data =[]
    for row in reader:
      #Utilizar un zip para unir el encabezado (header) y el resto de datos
      iterable = zip(header, row) #Hay una array como tupla
      #Creando diccionario
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict) #Tienendo como diccionario cada lista y contando con clave valor
    return data


if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])

#Transformar de una lista con formato de diccionarios.