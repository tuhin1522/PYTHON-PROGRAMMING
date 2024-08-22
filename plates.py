def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
  if not s[0].isalpha() or not s[1].isalpha():
    return False

  l = len(s)
  if l < 2 or l > 6:
    return False
  elif not s.isalnum():
    return False

  num=len(s)-1
  for char in s:
    if char.isnumeric():
      if char=='0':
        return False
      num = s.index(char)
      break
  for char in s:
    if s.index(char)<= num:
      pass
    else:
      if char.isalpha():
        return False
  
  return True

if __name__ == "__main__":
  main()
