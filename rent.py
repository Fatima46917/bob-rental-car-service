vehicles = []
class vehicles:
  def __init__(self, brand, model, year, daily_price):
    self.brand = brand
    self.model = model
    self.year = year
    self.__rental_price_per_day = daily_price

  def getrental_price_per_day (self):
    return self.__rental_price_per_day
  
  def setrental_price_per_day (self, vehicle_rent_price):
    self.__rental_price_per_day = vehicle_rent_price

  def display(self):
    print (f"brand :{self.brand}")
    print (f"model : {self.model}")
    print (f"year:{self.year}")
    print (f"rental_price_per_day:{self.__rental_price_per_day}")


  def rental_cost_per_days (self, number_of_days):
    self.number_of_days = number_of_days
    print(self.number_of_days * self.__rental_price_per_day)

class car (vehicles) :
  def __init__(self, brand, model, year, daily_price, seating_capacity):
    super().__init__(brand, model, year, daily_price)
    self.seating_capacity = seating_capacity

  def display(self):
   super().display()
   print(f"seating_capacity:{self.seating_capacity}")

  
class bike (vehicles):
  def __init__(self, brand, model, year, daily_price, engine_capacity):
    self.engine_capacity = engine_capacity
    super().__init__(brand, model, year, daily_price)

  def display(self):
    super().display()
    print(f"engine_capacity:{self.engine_capacity}")
  


vehicle1 = car ("Toyota", "corolla", 2020, "50$/day", 5)
vehicle1.display()
print("================")
vehicle2 = bike("yamaha", "R1", 2019, "30$/day", "998cc")
vehicle2.display()




