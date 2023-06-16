def is_valid_iterable(iterable):
    try:
        iter(iterable)
        return True
    except TypeError:
        return False


def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
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
    return [function_to_apply(elem) for elem in iterable]
    
x = [1, 2, 3, 4, 5]
# Output:
print(list(ft_map(lambda t: t + 1, x)))
ft_map(lambda y: y + 2, 42)
