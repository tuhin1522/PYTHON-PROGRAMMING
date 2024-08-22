class Restaurant:
  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = 0

  def describe_restaurant(self):
    print(f"{self.restaurant_name} is a very beautiful restaurant.")
    print(f"It is a {self.cuisine_type} restaurant.")

  def open_restaurant(self):
    print(f"{self.restaurant_name} is always open.")

  def set_number_served(self, customers):
    self.number_served = customers

  def increment_number_served(self, customers):
    self.number_served += customers

class IceCreamStand(Restaurant):
  """Represent aspects of a restaurant, specific to ice-cream."""
  def __init__(self, restaurant_name, cuisine_type):
    super().__init__(restaurant_name, cuisine_type)
    self.flavors = 100

  def display_flavors(self):
    """Display flavors in this restaurant"""
    print(f"Ice-cream price is {self.flavors}")





my_restaurant = Restaurant('Well Dev', 'FastFood')

print(f"My restaurant's name is {my_restaurant.restaurant_name}")
print(f"My restaurant type is {my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# -------------------------------------
my_restaurant.number_served = 23
print(my_restaurant.number_served)

my_restaurant.set_number_served(25)
print(my_restaurant.number_served)

my_restaurant.increment_number_served(200)
print(my_restaurant.number_served)

# -------------------------------------------------
my_ice = IceCreamStand('Well Dev', 'FastFood')
my_ice.describe_restaurant()
my_ice.display_flavors()
