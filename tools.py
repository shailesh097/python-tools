import math

def reverse_a_number(number: int) -> int:
	"""This function takes a number and reverses it.
	Args:
		number (int): Enter the number to reverse.
	Returns:
		int: Number after it is reversed.
	"""
	str_number = str(number)
	reverse = str_number[::-1]
	return int(reverse)

def is_armstrong(number: int) -> bool:
	"""This function checks if a number is armstrong or not.

	Args:
		number (int): The number to be checked.

	Returns:
		bool: Returns True if the 'number' is armstrong.
	"""
	to_string = str(number)
	number_len = len(to_string)

	sum_digits = 0

	for digit in to_string:
		sum_digits += int(digit) ** number_len
	
	return sum_digits == number

def is_prime(number: int) -> bool:
	"""Check if the "number" is prime or not.
	Args:
		number (int): The number to be checked.
	Returns:
		True: If the number is prime.
		False: If the number is not prime. 
	"""
	if number < 2:
		return False
	
	for i in range(2, int(math.sqrt(number)) + 1):
		if number % i == 0:
			return False

	return True

def n_fibonacci(number: int) -> list:
	"""Returns the list of "number" of fibonacci series items starting from 0.
	Args:
		number (int): Number of fibonacci number to return in the list. (number>0)
	Returns:
		list: n number of fibonacci number.
	"""
	a, b = 0, 1
	result = []
	while len(result)<n:
		result.append(n)
		a, b = b, a+b
	return result

def is_palindrome(var) -> bool:
	"""Checks if the given input is palindorme or not.
	Args:
		var (int/str): Input to check for palindorme.
	Raises:
		Exception: Can check only for string and integer type.
	Returns:
		True: If the given input is palindrome.
		False: If the given input is not palindrome.
	"""
	if type(var) == 'str':
		reverse = var[::-1]
	elif type(var) == 'int':
		to_str = str(var)
		reverse = to_str[::-1]
	else:
		raise Exception("Can only test for string and integer. Try changing the input to either integer or string.")
	
	return var == reverse

def is_binary(number: int) -> bool:
	"""Checks if the given input number is binary or not.
	Args:
		var (int): Number to check.	
	Returns:
		True: If the number is binary.
		False: If the number is not binary.
	"""
	to_string = str(var)
	
	for each_number in string:
		if each_number != '0' and each_number != '1':
			return False

	return True