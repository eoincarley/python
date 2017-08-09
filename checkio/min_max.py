import types

#///////// Top answer on Checkio /////////
def get_first_from_sorted(args, key, reverse):
    if len(args) == 1:
        args = iter(args[0])
    return sorted(args, key=key, reverse=reverse)[0]
​
def minio(*args, key=None):
    return get_first_from_sorted(args, key, False)
​
​
def maxio(*args, key=None):
    return get_first_from_sorted(args, key, True)

#////////////////////////////////////////

def arrange_args(args, key):

    if len(args)==1: 
        if type(args[0]) is types.GeneratorType: args = [tuple(args[0])]
        orig_args=[y for x in args for y in x]
        if type(orig_args[0])==str: 
            args = [key(ord(x)) for x in orig_args]
        else:  
            args = [key(y) for x in args for y in x]
    else: 
        orig_args = [x for x in args]
        args = [key(x) for x in args]

    return orig_args, args    


def min(*args, **kwargs):
    if kwargs: 
        key = kwargs.get("key", None) 
    else: 
        key=lambda x: x

    orig_args, args = arrange_args(args, key)


    min_val = args[0]
    for i in args: 
        if i<min_val: min_val=i

    min_val = orig_args[args.index(min_val)]        

    return min_val


def max(*args, **kwargs):
    if kwargs: 
        key = kwargs.get("key", None) 
    else: 
        key=lambda x: x

    orig_args, args = arrange_args(args, key)

    max_val = args[0]
    for i in args: 
        if i>max_val: max_val=i 

    max_val = orig_args[args.index(max_val)]    

    return max_val


#///////////////////////////////////

print min(abs(i) for i in range(-10, 10))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"