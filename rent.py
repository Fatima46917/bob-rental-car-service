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
    
