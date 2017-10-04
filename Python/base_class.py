
class MySum(object):

    def __call__(self, numA, numB):
        return numA + numB

mysum = MySum()

example = mysum(4, 5)

print(type(MySum))

print(type(mysum))

print(example)

print(type(type))

print(mysum.__doc__)
print(mysum.__dict__)

# c bindings, c-code, control code

# same as def mysum():
    #lines of code