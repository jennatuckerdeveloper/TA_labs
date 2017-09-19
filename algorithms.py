from random import shuffle

nums = [i for i in range(1000)]

def find_short(find, list):  #what would actually make sense
    try:
        return list.index(find)
    except:
        return -1

def find(find, list):  # a linear search pattern
    for i in range(0, len(list) - 1):
        if list[i] == find:
            return i
    return -1

def find2(find, list): #another variation that's not as efficient
    for i in list:
        if i == find:
            answer = i
    return list.index(answer)

def binary_search(find, list):
    low = 0
    high = len(list) -1
    while low <= high:
        mid = (low + high) // 2
        # print(mid)
        spot = list[mid]
        if spot == find:
            return mid
        elif spot > find:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# print(binary_search(53, nums))

def factorial(x):
    ans = 1
    for i in list(range(x, 1, -1)):
        print(ans)
        ans = ans * i
    return ans

# print(factorial(13))

def recursive_factorial(x):
    if x == 0:
        return 1
    else:
        return x * recursive_factorial(x-1)

# print(recursive_factorial(4))

#Recursive string reversal

def reverse(string):
    if string == "":
        return string
    return reverse(string[1:]) + string[0]

# print(reverse("abc"))

shuffle(nums)
# print(nums)

def selection_sort(sort):
    place = 0
    indices = list(range(place, len(sort)))
    while place < (len(indices)):
        for i in indices:
            if sort[i] > sort[place]:
                sort[place], sort[i] = sort[i], sort[place]
        place += 1
    return sort

# selection_sort(nums)
# print(nums)

check = [8, 1, 9, 6, 3]
# selection_sort(check)
# print(check)



def merge(sort):
    mid = len(sort) // 2
    one = sort[:mid]
    two = sort[mid:]
    first = selection_sort(one)
    second = selection_sort(two)
    third = [0] * (len(sort))
    i1, i2, i3 = 0,0,0
    n1, n2 = len(first), len(second)

    while i1 < n1 and i2 < n2:
        print(i1, i2, i3, first, second, third)
        if first[i1] < second[i2]:
            third[i3] = first[i1]
            i1 = i1 + 1
        else:
            third[i3] = second[i2]
            i2 = i2 + 1
        i3 += 1
    while i1 < n1:
        third[i3] = first[i1]
        i1 += 1
        i3 += 1
    while i2 < n2:
        third[i3] = second[i2]
        i2 += 1
        i3 += 1
    return third

print(merge(check))