class vehicles:
  def __init__(self, vehicle, brand_model, year, rental_price_per_day):
    self.vehicle = vehicle
    self.brand_model = brand_model
    self.year = year
    self.rental_price_per_day = rental_price_per_day

vehicle1 = vehicles("car", "Toyota Corolla", 2020, "50$/day")
print(vehicle1.vehicle)
print(vehicle1.brand_model)
print(vehicle1.year)
print(vehicle1.rental_price_per_day)



 