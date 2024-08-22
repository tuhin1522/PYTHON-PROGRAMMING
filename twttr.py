def main():
  prompts = input("Input: ")
  short_twttr = convert(prompts)
  print(f"Output: {short_twttr}")

def convert(prompts):
  vowels = ['a', 'e', 'i', 'o', 'u']
  without_vowel = ""
  for word in prompts:
    if word.lower() not in vowels:
      without_vowel += word
  return without_vowel

if __name__ == "__main__":
  main()
