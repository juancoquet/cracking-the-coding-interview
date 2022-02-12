# 17.1 Add without plus
def add_without_plus(a, b):
	bit_length = max(a.bit_length(), b.bit_length())
	carry = False
	result = 0
	for i in range(bit_length + 1):
		a_bit = get_bit(a, i)
		b_bit = get_bit(b, i)
		added = a_bit ^ b_bit
		if carry:
			added = added ^ 1
		if (a_bit and b_bit) or ((a_bit != b_bit) and carry):
			carry = True
		else:
			carry = False
		if added == 1:
			result = set_bit(result, i)
	return result
		

def get_bit(num, i):
	mask = 1 << i
	if num & mask != 0:
		return 1
	else:
		return 0

def set_bit(num, i):
	return num | (1 << i)

