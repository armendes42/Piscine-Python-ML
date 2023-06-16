def is_valid_iterable(iterable):
    try:
        iter(iterable)
        return True
    except TypeError:
        return False

def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """
    # ... Your code here ...
    if not is_valid_iterable(iterable):
        print("The object is not iterable")
        return None
    value = iterable[0]
    if len(iterable) == 1:
        return value
    for elem in iterable[1:]:
        value = function_to_apply(value, elem)
    return value

lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))
ft_reduce(lambda u, v: u + v, 42)

