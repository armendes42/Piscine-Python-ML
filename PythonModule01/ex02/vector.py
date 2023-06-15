def is_float_list(lst):
    """Determine if object is list of floats"""
    if not isinstance(lst, list) or len(lst) == 0:
        return False
    for elem in lst:
        if not isinstance(elem, float):
            return False
    return True

def is_list_list(lst):
    """Determine if object is list of sublists of float"""
    if not isinstance(lst, list) or len(lst) == 0:
        return False
    for elem in lst:
        if not is_float_list(elem):
            return False
    return True

def is_rectangular(lst):
    """Determine if object is a list of sublists of same size"""
    if not is_list_list(lst):
        return False
    size = len(lst[0])
    for elem in lst:
        if len(elem) != size:
            return False
    return True

def is_range(tpl):
    """Determine if object is tuple that describes a range"""
    if not isinstance(tpl, tuple) or len(tpl) != 2:
        return False
    if isinstance(tpl[0], int) and isinstance(tpl[1], int) and tpl[0] < tpl[1]:
        return True
    return False


class Vector:
    def __init__(self, values):
        self.values = []
        if isinstance(values, list):
            if is_float_list(values):
                self.shape = (1, len(values))
                self.values.append(values.copy())
            elif is_list_list(values) and is_rectangular(values):
                self.shape = (len(values), len(values[0]))
                for elem in values:
                    self.values.append(elem.copy())
            else:
                raise ValueError("Invalid list for Vector")
        elif isinstance(values, int):
            self.shape = (values, 1)
            for i in range(values):
                self.values.append([float(i)])
        elif is_range(values):
            self.shape = (values[1] - values[0], 1)
            for i in range(values[0], values[1]):
                self.values.append([float(i)])
        else:
            raise ValueError("Invalid values for Vector")
        
    def __add__(self, other):
        new_vector = Vector(self.values)
        if isinstance(other, Vector) and self.shape == other.shape:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_vector.values[i][j] += other.values[i][j]
        else:
            raise ValueError("Invalid type for addition")
        return new_vector

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        new_vector = Vector(self.values)
        if isinstance(other, Vector) and self.shape == other.shape:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_vector.values[i][j] -= other.values[i][j]
        else:
            raise ValueError("Invalid type for substraction")
        return new_vector

    def __rsub__(self, other):
        return self.__sub__(other)

    def __truediv__(self, other):
        new_vector = Vector(self.values)
        if isinstance(other, int) or isinstance(other, float):
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_vector.values[i][j] /= other
        else:
            raise ValueError("Invalid type for division")
        return new_vector

    def __rtruediv__(self, other):
        raise ValueError("Can't divide by Vector")
    
    def __mul__(self, other):
        new_vector = Vector(self.values)
        if isinstance(other, int) or isinstance(other, float):
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_vector.values[i][j] *= other
        else:
            raise ValueError("Invalid type for multiplication")
        return new_vector
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __str__(self):
        txt = ("Vector values : " + str(self.values) + "\nShape : " + str(self.shape))
        return txt
    
    def __repr__(self):
        txt = str(self.values) + " : " + str(self.shape)
        return txt
    
    def dot(self, other):
        """Returns the dot product of two vectors"""
        if self.shape != other.shape:
            raise ValueError("Dot product requires two vectors with the same shape")
        dot_product = 0
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                dot_product += self.values[i][j] * other.values[i][j]
        return dot_product
    
    def T(self):
        transposed_values = []
        for j in range(self.shape[1]):
            transposed_row = [self.values[i][j] for i in range(self.shape[0])]
            transposed_values.append(transposed_row)
        return Vector(transposed_values)
    