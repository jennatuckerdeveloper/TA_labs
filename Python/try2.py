def return_two(num):
    this = num + 1
    that = num + 3
    return this, that

one, two = return_two(5)
print(one, two)