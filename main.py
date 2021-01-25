from store.start import Store
from stock.start import Stock
import random


def initialize():
  """ 
    This is a test method to initialize a sample store
    with test data and a couple dummy stuffs
  """

  print()
  dummy_names = ['Vitamin C', 'Monitor', "CPU", "Board", "Laptops", 'Desktops']
  store = Store(products = [])
  for i in range(0, 50):
    new_stock = Stock(dummy_names[random.randint(0, len(dummy_names))], 'Some really silly stuff', random.random() * 1000)
    random.
  


if __name == '__main__':
  initialize()