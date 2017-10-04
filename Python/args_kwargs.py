#*args and **kwargs (notice the second * in ** to signify a key-value pair, since the word is a variable)
#The asterix and double asterix allows a variable number of parameters to be passed into a function.  End of.

def practice (*args):
    for arg in args:
        for i in arg:
            print(i)




list1 = ['red', 'blue', 'orange']
list2 = [1, 3, 5, 7, 9]
#
# practice(list1)
# practice(list2)
practice(list1, list2)

def test (**kwargs):
    for i, j in kwargs.items():
        print(i, j)

test(name='tim', sport='football', roll=19)