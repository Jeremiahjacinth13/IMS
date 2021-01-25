class Stock:
  def __init__(self, name, common_name, price):
    self.name = name
    self.common_name = common_name
    self.price = price

  def __str__(self):
    return f"Name: {self.name}; Price: {self.price}"