vehicles = []
class vehicles:
  def __init__(self, brand, model, year, price):
    self.brand = brand
    self.model = model
    self.year = year
    self.__rental_price_per_day = price

  def display(self):
    print (f"brand :{self.brand}")
    print (f"model : {self.model}")
    print (f"year:{self.year}")
    print (f"rental_price_per_day:{self.__rental_price_per_day}")


  def rental_cost_per_days (self, number_of_days):
    self.number_of_days = number_of_days
    print(self.number_of_days * self.__rental_price_per_day)

class car (vehicles) :
  def __init__(self, brand, model, year, price, seating_capacity):
    self.seating_capacity = seating_capacity
    super().__init__(brand, model, year, price)

class bike (vehicles):
  def __init__(self, brand, model, year, price, engine_capacity):
    self.engine_capacity = engine_capacity
    super().__init__(brand, model, year, price)

