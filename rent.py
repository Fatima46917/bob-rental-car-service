vehicles = []
class vehicles:
  def __init__(self, brand, model, year, rental_price_per_day):
    self.brand = brand
    self.model = model
    self.year = year
    self.rental_price_per_day = rental_price_per_day

  def display(self):
    print (f"brand :{self.brand}")
    print (f"model : {self.model}")
    print (f"year:{self.year}")
    print (f"rental_price_per_day:{self.rental_price_per_day}")


  def rental_cost_per_days (self, number_of_days):
    self.number_of_days = number_of_days
    print(self.number_of_days * self.rental_price_per_day)

class car (vehicles) :
  def __init__(self):
    self.__rental_price_per_day = 50 

  def getrental_price_per_day (self):
    return self.__rental_price_per_day

  def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
    self.seating_capacity = seating_capacity
    super().__init__(brand, model, year, rental_price_per_day)

class bike (vehicles):
  def __init__(self):
    self.__rental_price_per_day = 30

  def getrental_price_per_day(self) :
    return self.__rental_price_per_day
  

  def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
    self.engine_capacity = engine_capacity
    super().__init__(brand, model, year, rental_price_per_day)

