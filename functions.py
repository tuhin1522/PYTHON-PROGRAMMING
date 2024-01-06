def message():
    print("Welcome to PYnative")

# call function using its name
message()

def course_func(name, course_name):
    print("Hello", name, "Welcome to PYnative")
    print("Your course name is", course_name)

# call function
course_func('John', 'Python')

def calculator(a, b):
    return a+b

result = calculator(5, 10)
print("Result :",result)

def factorial(x):
    """This function returns the factorial of a given number."""
    return x

# access doc string
print(factorial.__doc__)

def is_even(list1):
    even_list = []
    for i in list1:
        if i%2==0:
            even_list.append(i)
    return even_list

my_list = is_even([2,3,4,5,6,7,8])
print(my_list)

# Global variable
x = 5

# defining 1st function
def function1():
    print("Value in 1st function :", x)

# defining 2nd function
def function2():
    # Modify global variable using global keyword
    global x
    x = 555
    print("Value in 2nd function :", x)

# defining 3rd function
def function3():
    print("Value in 3rd function :", x)

function1()
function2()
function3()

def outer_func():
    x = 777

    def inner_func():
        # local variable now acts as global variable
        nonlocal x
        x = 700
        print("value of x inside inner function is :", x)

    inner_func()
    print("value of x inside outer function is :", x)

outer_func()

def addition(*numbers):
    total = 0
    for no in numbers:
        total = total + no
    print("Sum is:", total)


# 0 arguments
addition()

# 5 arguments
addition(10, 5, 2, 5, 4)


# 3 arguments
addition(78, 7, 2.5)

l = [2,5,4,11,22,32,444,55]
my = list(filter(lambda x: x%2==0, l))
print("The Even number : ",my)

p, q, r = 10, 20 ,30
print(p, q, r)


x = 36 / 4 * (3 +  2) * 4 + 2
print(x)

def calculate (num1, num2=4):
  res = num1 * num2
  print(res)

calculate(5, 6)

var= "James Bond"
print(var[2::-1])