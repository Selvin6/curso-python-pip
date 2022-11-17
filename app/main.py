#Módulo propio creado en una carpeta
import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent']== 'South America', data)) #Filtrar datos por south america

  countries = list(map(lambda x: x['Country/Territory'], data)) #Selecciona toda la columna de country para obtener todos los paises
  percentages = list(map(lambda x: x['World Population Percentage'], data)) #Posterior elegimos la columna que necesitamos como valor, como solo se necesita una columna también se utiliza un map
  charts.generate_pie_cahrt(countries, percentages)


  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)

if __name__ == '__main__':
  run()
  