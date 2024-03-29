import utils as utils

data = [
  {
    'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }
]

def run():
  keys, values = utils.get_population()
  print(keys)
  print(values)


  result = utils.population_by_country(data, 'Colombia')
  print(result)

""" si es ejecutado desde la terminal, entonces corres esto, si es ejecutado desde otro lado, no lo ejecutas """
if __name__ == '__main__': 
  run()