def is_valid_iterable(iterable):
    try:
        iter(iterable)
        return True
    except TypeError:
        return False

def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable.
        None if the iterable can not be used by the function.
    """
    # ... Your code here ...
    if not is_valid_iterable(iterable):
        print("The object is not iterable")
        return None
    return [item for item in iterable if function_to_apply(item)]

x = [1, 2, 3, 4, 5]
# Output:
print(list(ft_filter(lambda dum: not (dum % 2), x)))
ft_filter(lambda y: y + 2, 42)