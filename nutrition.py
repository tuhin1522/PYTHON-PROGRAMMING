fruits = {'apple': 130, 'avocado': 50, 'banana': 110, 'cantaloupe': 50, 'grapefruit': 60, 'grapes': 90, 'honeydew melon': 50, 'kiwifruit': 90, 'lemon': 15, 'lime': 20, 'nectarine': 60, 'orange': 80, 'peach': 60, 'pear': 100, 'pineapple': 50, 'plums': 70, 'strawberries': 50, 'sweet cherries': 100, 'tangerine': 50, 'watermelon': 80}

def main():
  item = input("Item: ")
  calorie = calories(item)

def calories(item):
  found = False
  for key, value in fruits.items():
    if item.lower() == key.lower():
      print(f"Calories: {value}")
      found = True
  if found:
    return

if __name__ == "__main__":
  main()
