def fizzbuzz(a):
	if(a%15 == 0):
		return "FizzBuzz"
	elif(a%3 == 0):
		return "Fizz"
	elif(a%5 == 0):
		return "Buzz"
	else:
		return a

print(fizzbuzz(30))
print(fizzbuzz(9))
print(fizzbuzz(25))
print(fizzbuzz(4))