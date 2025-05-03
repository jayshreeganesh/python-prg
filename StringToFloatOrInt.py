# Solution 1 - Parse string into Integer

string = "12345"

print(type(string))
int_str = int(string)
print(type(int_str))

# Solution 2 - Parse string into Float

temp_string = "123.45"
print(type(temp_string))
print(temp_string)
float_string = float(temp_string)
print(type(float_string))
print(float_string)

# Solution 3 - Parse Sstring Float Numericals into Integer

other_string = "123.45"
print(type(other_string))
float_int_str = int(float(other_string))
print(type(float_int_str))