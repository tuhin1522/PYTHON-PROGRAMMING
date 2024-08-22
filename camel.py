def main():
  name = input("camelCase: ")
  result = convert_camel(name)
  print(f"snake_case: {result}")

def convert_camel(name):
  ans = ""
  ans = name[0].lower()
  for i in range(1,len(name)):
    if name[i].isupper():
      ans += "_" + name[i].lower()
    else:
      ans += name[i]

  return ans


if __name__ == "__main__":
  main()