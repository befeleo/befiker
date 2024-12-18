def modify_value(x):
    x = x + 5
    print(f"Inside function: x = {x}")


num = 10
print(f"Before function call: num={num}")
modify_value(num)
print(f"After function call: num = {num}")
