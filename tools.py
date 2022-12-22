
def reverse_a_number(number):
	"""This function takes a number and reverses it.

	Args:
		number (int): Enter the number to reverse.

	Returns:
		int: Number after it is reversed.
	"""
	reverse = 0
	while n!=0:
		reverse = reverse*10 + n%10
		n = (n//10)
	return reverse

def is_armstrong(number):
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

