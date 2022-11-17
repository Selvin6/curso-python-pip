#Se puede colocar un alias para acortar la libreria y utilizarla
import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots() #Fig por la figura 
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png') #para guardar la imagen
  plt.close() #Para cerrar 

def generate_pie_cahrt(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels) #Indicando oel argmento labels sea labels, es lo que la guia muestra que debe hacerse
  ax.axis('equal') #Para asignar que esa redondo
  plt.savefig('pie.png')
  plt.close()
  
#Generando un barchar de forma dinámica
if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  #generate_bar_chart(labels, values) => Gráfica de barras
  #generate_pie_cahrt(labels, values) => Gráfica de círculo