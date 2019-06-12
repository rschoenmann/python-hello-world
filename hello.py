from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

msg = "Hello Python World"
print(msg)

print("This line will be printed")

print("hello world")

myint = 7
print(myint)

myfloat = 7.5
print(myfloat)

one = 1
two = 2
print(1+2)

a, b = 3, 4
print(a)

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])

for x in mylist:
	print(x)

number = 1+2*3/4
print(number)

remainder = 11 %3
print(remainder)

lotsofhellos = "hello" * 10
print(lotsofhellos)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7,9]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3]*3)

name = "Rachel"
print("Hello, %s!" % name)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

astring = "Hello World!"
print(astring[::-1])

#conditionals: Python uses indentation instead of brackets to define code blocks
x = 2
if x == 2:
	print("x equals two!")
else:
	print("x doesn't equal two.")


# This is a for loop:
# primes = [2,3,5,7]
# for prime in primes:
# 	print(prime)

# you can also use loops to iterate over a sequence of numbers using range and xrange
# for x in range(5):
# 	print(x)

# for x in range(3,6):
# 	print(x)

# for x in range(3,8,2):
# 	print(x)

# Prints out 0,1,2,3,4

# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break

# # Prints out only odd numbers - 1,3,5,7,9
# for x in range(10):
#     # Check if x is even
#     if x % 2 == 0:
#         continue
#     print(x)

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
	return (a + b)

my_function()
my_function_with_args("Rachel", "good luck with Python!")
x = sum_two_numbers(2,2)
print(x)


