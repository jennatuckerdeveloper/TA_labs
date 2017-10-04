def al_to_la_R(string):
    if string == "":
        return string
    else:
        return al_to_la_R(string[2:]) + string[1] + string[0]

print(al_to_la_R("alalalalalalalal"))

def multiply_R(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] * multiply_R(nums[1:])

print(multiply_R([5,4,7]))

def fib_seq(n):

    #create a sequence as long as n
    #for every place in sequence, it equals the last two numbers

    skeleton = list(range(n+1))
    skeleton[0] = 1
    skeleton[1] = 1
    for i in skeleton:
        if i > 1:
            skeleton[i] = skeleton[i-1] + skeleton[i-2]

    return skeleton[n-1]

print(fib_seq(7))
#
# #derive Golden Ratio
# for i in range(1,51):
#     print(fib_seq(i+1) / fib_seq(i))

def fib_seq_R(x):
    if x < 1:
        return
    else:
        return fib_seq(x-1) + fib_seq(x-2)

print(fib_seq_R(7))

def factorial(x):
    # take a number
    # if that num is 0, return 1
    # else multiply all nums in range of that number (excluding 0)
    # running total cannot be 0, because we are multiplying - use 1
    ans = 1
    if x == 0:
        return ans
    else:
        for i in range(1, x+1):
            ans = (ans * i)

    return ans

print(factorial(4))

def factorial_R(x):
    if x == 0:
        return 1
    else:
        return factorial_R(x-1) * x
print(factorial_R(4))

def add_R(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + add_R(nums[1:])

print(add_R([4,3,8]))

