from arithmetic import add, subtract, multiply, divide
a = 6
b = 5
val = add(a,b)
if (val != 10):
    print(f"There's a problem with the add function. {a} + {b} should be 10 but the function returned {val}")

val = subtract(a,b)
if (val != 2):
    print(f"There's a problem with the subtract function. {a} - {b} should be 2 but the function returned {val}")