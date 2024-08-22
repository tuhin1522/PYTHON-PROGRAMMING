class User:
  """Initialize personal information"""
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    self.login_attempts = 1

  def describe_user(self):
    print(f"My full name is {self.first_name} {self.last_name}.")

  def greet_user(self):
    print(f"{self.first_name} {self.last_name} is a honest man.")

  def increment_login_attempts(self, login_users):
    self.login_attempts += login_users

  def reset_login_attempts(self):
    self.login_attempts = 0

class Privileges:
  """A simple admin post control"""
  def __init__(self):
    self.privileges = ["can add post", "can delete post", "can ban user"]

  def show_privileges(self):
    print(f"This is privileges list: {self.privileges}")

class Admin(User):
  """Represented in user administrator panel"""
  def __init__(self, first_name, last_name):
    super().__init__(first_name, last_name)
    self.privileges = Privileges()






person1 = User('Tuhin', 'Islam')
person2 = User('Tamjid', 'Hossen')

person1.describe_user()
person1.greet_user()

print()
person2.describe_user()
person2.greet_user()


# ------------------------------------
person1.increment_login_attempts(1)
print(person1.login_attempts)

person1.reset_login_attempts()
print(person1.login_attempts)

# -----------------------------------------
my_profile = Admin('Akber', 'Hossen')
my_profile.describe_user()

my_profile.privileges.show_privileges()