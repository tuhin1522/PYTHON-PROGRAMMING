def main():
  price = 50
  due = price
  while 0 < price:
    print(f"Amount Due: {due}")
    cent = int(input("Insert cent: "))
    if cent == 25 or cent == 10 or cent == 5:
      due -= cent
    price = due

  if due < 0:
    due = -due
  print(f"Change Owed: {due}")

if __name__ == "__main__":
  main()