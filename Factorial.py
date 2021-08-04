def factorial(int):
    if int == 1: return 1
    if int > 0: return int * factorial(int - 1)

print(factorial(1))
print(factorial(4))
