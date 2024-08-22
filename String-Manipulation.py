my_city = "New York"
print(type(my_city))

my_city = 'New York'
print(type(my_city))


my_city = str('New York')
print(type('New York'.__str__()))

#Concatenate
word1 = 'New '
word2 = 'York'
print(word1 + word2)

#Selecting a char
word = "Rio de Janeiro"
char = word[0]
print(char)

#Size of a String
print(len(word))

#Replacing
rep = "Rio de Janeiro".replace('Rio', 'Mar')
print(rep)

#count
print(word.count(' '))

#Repeating a string
words = "Tokyo " * 3
print(words)

#How to Split a String
#Example 1: whitespaces as delimiters
my_phrase = "let's go to the beach"
my_words = my_phrase.split(" ")
#my_words = my_phrase.split()

for word in my_words:
  print(word, end=",")
print()
print(my_words)

#Example 2: passing different arguments as delimiters
my_csv = "mary;32;australia;mary@email.com"
my_data = my_csv.split(";")
for word in my_data:
  print(word)

print(my_data[3])

#How to remove all white spaces in a string
import re
phrase = ' Do  or do   not   there  is   no  try'
phrase_no_space = re.sub(r'\s+', '',phrase)

print(phrase)
print(phrase_no_space)

#Multiline Strings
#Triple Quotes
long_text = """This is a multiline,
a long string with lots of text,
I'm wrapping it in triple quotes to make it work."""
print(long_text)
long_text = '''This is a multiline,
a long string with lots of text,
I'm wrapping it in triple quotes to make it work.'''
print(long_text)

#Parenthesis
long_text = ("This is a multiline, "
"a long string with lots of text "
"I'm wrapping it in triple quotes to make it work.")
print(long_text)

#Backlashes.
long_text = "This is a multiline, \n\n" \
"a long string with lots of text \n\n" \
"I'm using backlashes to make it work."
print(long_text)

#lstrip(): removing spaces and chars from the beginning of a string
regular_text = "      This is a regular text."
no_space_begin_text = regular_text.lstrip()
print(regular_text)
print(no_space_begin_text)

# Removing Chars
regular_text = "$@G#This is a regular text.."
clean_begin_text = regular_text.lstrip('$@G#')
print(clean_begin_text)

#rstrip(): removing spaces and chars from the end of a string
regular_text = "This is a regular text.          "
no_space_end_text = regular_text.rstrip()
print(regular_text)
print(no_space_end_text)

#strip(): removing spaces and chars from the beginning and end of a string
regular_text = "    This is a regular text.      "
no_space_text = regular_text.strip()
print(no_space_text)

#example2
regular_text = "AbC#This is a regular text.$@G#"
clean_text = regular_text.strip("AbC#$@G")
print(clean_text)

#String lowercase
regular_text = "This is a Regular TEXT."
lowercase_text = regular_text.lower()
print(lowercase_text)

#String uppercase
regular_text = "This is a Regular TEXT."
uppercase_text = regular_text.upper()
print(uppercase_text)

#String Title case
regular_text = "This is a Regular TEXT."
titlecase_text = regular_text.title()
print(titlecase_text)

#String swapcase
regular_text = "This is a Regular TEXT."
swapcase_text = regular_text.swapcase()
print(swapcase_text)

# Checking if a string is empty
my_string = ''
if not my_string:
  print("String is empty.")

# Checking if the string is not empty
my_string = 'amazon, microsoft'
if my_string:
  print("My String is not empty!")

# rjust(): right-justified String
word = 'beach'
number_spaces = 32
word_justified = word.rjust(number_spaces)
print(word_justified)

# The rjust() also accepts a specific char as a parameter to fill the remaining space.
word = 'beach'
number_chars = 32
char = '$'
word_justified = word.rjust(number_chars, char)
print(len(word_justified))

# ljust(): left-justified string
word = 'beach'
number_spaces = 32
word_justified = word.ljust(number_spaces)
print(word_justified)

#isalnum(): checking alphanumeric only in a string
word = 'beach'
print(word.isalnum())

word = '32'
print(word.isalnum())

word = 'beach32'
print(word.isalnum())

word = 'Favorite number is 32'
print(word.isalnum())

word = '$#beach32!'
print(word.isalnum())

# isprintable(): checking printable characters in a string
text = ''
print(text.isprintable())

text = 'This is a regular text.'
print(text.isprintable())

text = '          '
print(text.isprintable())

text = '\f\v\r\t\n'
print(text.isprintable())

# isspace(): checking white space only in a string
text = ' '
print(text.isspace())

text = ' \f\n\r\t\v'
print(text.isspace())

text = ''
print(text.isspace())

text = 'This is a regular text.'
print(text.isspace())

# startswith(): checking if a string begins with a certain value
phrase = 'This is a regular text.'
print(phrase.startswith('This is'))
print(phrase.startswith('text'))
print(phrase.startswith('regular', 10))
print(phrase.startswith('regular', 10,22))
print(phrase.startswith('regular', 10, 15))
print(phrase.startswith(('regular', 'This')))
print(phrase.startswith(('regular', 'text')))
print(phrase.startswith(('regular', 'text'), 10, 22))

# endswith(): check if a string ends with a certain value
phrase = "This is a regular text"
print(phrase.endswith('regular text'))
print(phrase.endswith('This'))
print(phrase.endswith('This is', 0, 7))
print(phrase.endswith('regular', 0, 17))
print(phrase.endswith('regular', 0, 15))
print(phrase.endswith(('regular', 'This', 'text')))
print(phrase.endswith(('regular', 'is')))
print(phrase.endswith(('regular', 'text'), 10, 22))

# capitalize(): first character only to upper case in a string
text = 'this is a regular text'
print(text.capitalize())

text = 'THIS IS A REGULAR TEXT'
print(text.capitalize())

text = 'THIS $ 1S @ A R3GULAR TEXT!'
print(text.capitalize())
text = '3THIS $ 1S @ A R3GULAR TEXT!'
print(text.capitalize())

# isupper(): checking upper case only in a string
text = 'This is a regular text'
print(text.isupper())
text = 'THIS IS A REGULAR TEXT'
print(text.isupper())
text = 'THIS $ 1S @ A R3GULAR TEXT!'
print(text.isupper())

# islower(): checking lower case only in a string
text = 'This is a regular text'
print(text.islower())
text = 'this is a regular text'
print(text.islower())
text = 'this $ 1s @ a r3gular text!'
print(text.islower())

# join(): join items of an iterable into one string
# join(): Strings
my_string = 'beach'
print('$'.join(my_string))

# join(): Lists
my_list = ['bmw', 'ferrari', 'mclaren']
print('$'.join(my_list))

# join(): Tuples
my_tuple = ('bmw', 'ferrari', 'mclaren')
print('$'.join(my_tuple))

# join(): Sets
my_set = {'bmw', 'ferrari', 'mclaren'}
print('|'.join(my_set))

# join(): dictionaries
my_dict = {'bmw': 'BMW I8', 'ferrari': 'Ferrari F8', 'mclaren': 'McLaren 720S'}
print(','.join(my_dict))

# splitlines(): splitting a string at line breaks
my_string = 'world \n cup'
print(my_string.splitlines())
print(my_string.splitlines(True))

# isnumeric(): checking numerics only in a string
word = '32'
print(word.isnumeric())
print("\u2083".isnumeric()) 
print("\u2169".isnumeric()) 

word = 'beach'
print(word.isnumeric())

word = 'number32'
print(word.isnumeric())

word = '1 2 3'
print(word.isnumeric())

word = '@32$'
print(word.isnumeric())

# isdigit(): checking digits only in a string
word = '32'
print(word.isdigit())

print("\u2083".isdigit()) #unicode for subscript 3

word = 'beach'
print(word.isdigit())

word = 'number32'
print(word.isdigit())

word = '1 2 3' 
print(word.isdigit())

word = '@32$'
print(word.isdigit())

# isdecimal(): checking decimals only in a string
word = '32'
print(word.isdecimal())
#output: True
word = '954'
print(word.isdecimal())
#output: True
print("\u2083".isdecimal()) #unicode for subscript 3
#output: False
word = 'beach'
print(word.isdecimal())
#output: False
word = 'number32'
print(word.isdecimal())
#output: False
word = '1 2 3' #notice the space between chars
print(word.isdecimal())
#output: False
word = '@32$' #notice the special chars '@' and '$'
print(word.isdecimal())
#output: False

# isalpha(): checking letters only in a string
word = 'beach'
print(word.isalpha())

word = '32'
print(word.isalpha())

word = 'number31'
print(word.isalpha())

word = 'Favorite number is blue' #notice the space between words
print(word.isalpha())
#output: False
word = '@beach$' #notice the special chars '@' and '$'
print(word.isalpha())

# istitle(): checking if every word begins with an upper case char in a string
text = 'This is a regular text'
print(text.istitle())
#output: False
text = 'This Is A Regular Text'
print(text.istitle())
#output: True
text = 'This $ Is @ A Regular 3 Text!'
print(text.istitle())
#output: True

# expandtabs(): set the number of spaces for a tab in a string
my_string = 'WORL\tD'
print(len(my_string.expandtabs()))

my_string = 'WORL\tD\tCUP'
print(my_string.expandtabs())

# Custom Tabsize
my_string = 'B\tR'
print(my_string.expandtabs(4))
my_string = 'B\tR'
print(my_string.expandtabs(6))

# center(): centered string
word = 'beach'
number_spaces = 32
word_centered = word.center(number_spaces)
print(word_centered)

word = 'beach'
number_chars = 33
char = '$'
word_centered = word.center(number_chars, char)
print(word_centered)

# zfill(): add zeros to a string
word = 'beach'
size_string = 32
word_zeros = word.zfill(size_string)
print(word_zeros)

# find(): check if a string has a certain substring
phrase = "This is a regular text"
print(phrase.find('This'))
print(phrase.find('regular'))
print(phrase.find('text'))
print(phrase.find('train'))
print(phrase.find('This', 0, 7))

# Removing a Prefix or a Suffix in a String
# lstrip() vs removeprefix() and rstrip() vs removesuffix()
word = 'hubbubbubboo'
print(word.lstrip('hub'))
print(word.removeprefix('hub'))

word = 'peekeeneenee'
print(word.rstrip('nee'))
print(word.removesuffix('nee'))

# How to reverse a string
my_string = "ferrari"
my_string_reversed = my_string[::-1]
print(my_string)
print(my_string_reversed)
