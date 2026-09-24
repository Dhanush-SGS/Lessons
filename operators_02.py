"""  
This page explains various operators and operator families
"""

# Initial Variables
a = 2
b = 2
x = 9
y = 7



print("\n")
##############################################
# Arithmetic Operators
c = a**b  # you can do that with +, -, /, *, **
print(f"c = {c}")

d = a % b # modulo operator gives remainder of the divsion
print(f"d = {d}")

e = a // b # floor division takes the integer part eliminating the decimal part
f = x // y
print(f"e = {e}")
print(f"f = {f}")



print("\n")
##############################################
# Comparision Operators
print(f"a==b verification is: {a == b}")
print(f"a<=b verification is: {a <= b}")
print(f"a>=b verification is: {a >= b}")
print(f"a!=b verification is: {a != b}")




print("\n")
##############################################
# Logical Operators
bit1 = 0
bit2 = 1

print("AND operation: {bit1 and bit2}")
print("OR operation: {bit1 or bit2}")
print("NOT operation: {not bit2}")




print("\n")
##############################################
# Assignment Operators
v1 = 0
v1 += 1
print(f"Add and assign v1: {v1}")

v2 = 0
v2 -= 1
print(f"Subtract and assign v2: {v2}")


v3 = 4
v3 *= 2
print(f"Multiply and assign v3: {v3}")

v4 = 10
v4 /= 2
print(f"Divide and assign v4: {v4}")

v5 = 5
v5 //= 2 
print(f"Flooring and assign v5: {v5}")

v6 = 0
v6 **= 0
print(f"Exponent and assign v6: {v6}")
