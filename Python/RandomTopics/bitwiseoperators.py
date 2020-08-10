# Bitwise Operators
# Complement(~)
# And(&)
# Or(|)
# XOR(^)
# Left Shift(<<)
# Right Shift(>>)

# Complement
# Reverses your binary format
# 12 = 00001100
print(~12, )  # -13, or 11110011
print(~45, "\n")

# If you want to find a negative number:
# Negative binary = 2's complement
# 2's complement = 1's complement + 1

# For example: 13 = 00001101
# 1's Complement of 13 = 11110010
# 2's Complement of 13 = 11110010 + 1
# 2's Complement of 13 = 11110011
# -13 = 2's Complement of 13 = 11110011

# To get the positive number from the 2's complement
# Subtract 1 and take the complement.

# Bitwise And (&)
print(12 & 13)
# 12(00001100)
# 13(00001101)
# And means both bits in a position
# have to be 1 for the result's bit to be 1
# Answer: 00001100, or 12.
print(25 & 30, "\n")
# 00011001 (25) & 00011110 (30)
# = 00011000 (24)

# Bitwise Or (|)
print(12 | 13, "\n")
# 00001100 | 00001101
# = 00001101 (13)

# Bitwise XOR/Exclusive Or (^)
print(12 ^ 13, "\n")
# 00001100 ^ 00001101
# = 00000001

# Left Shift
print(10 << 2, "\n")
# Shifts bits to the left, add 0's on to the end.
# 00001010 (10) << 2
# 00101000 (2)

# Right Shift
print(10 >> 2, "\n")
# Shifts bits to the right, lose bits.
# 00001010 (10) >> 2
# 00000010 (2)

