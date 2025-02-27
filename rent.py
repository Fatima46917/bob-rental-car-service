class vehicles:
  def __init__(self, vehicle, brand_model, year, rental_price_per_day):
    self.vehicle = vehicle
    self.brand_model = brand_model
    self.year = year
    self.rental_price_per_day = rental_price_per_day

vehicle1 = vehicles("car", "Toyota Corolla", 2020, "50$/day")
vehicle2 = vehicles("bike", "Yamaha R1", 2019, "30$/day")

vehicle = {
  "car" : "Toyota Corolla",
  "year": "2020",
  "seats": "5",
  "rental_price_per_day" : "50$/day"
}
print(vehicle)

bike = {
  "Bike" : "Yamaha R1",
  "year" : "2019",
  "rental_price_per_day" : "30$/day",
  "engine" : "998cc"
}
print(bike)







 