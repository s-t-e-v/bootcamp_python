class Vector():

    def __init__(self, input):
        if type(input) == int:
            self.values = [[float(i)] for i in range(input)]
        elif type(input) == tuple:
            self.values = [[float(i)] for i in range(input[0], input[1])]
        elif type(input) == list:
            self.values = input
        else:
            raise NotImplementedError("This type of input is not handled.")
        nb_elt = len(self.values)
        self.shape = (len(self.values), len(self.values[0]))

    def dot(self, v):
        if self.shape != v.shape:
            raise ValueError("Vectors does not have the same shape")
        return sum(
                sum(x1 * x2 for x1, x2 in zip(row1, row2))
                for row1, row2 in zip(self.values, v.values)
        )

    def T(self):
        return Vector(
            [
                [row[i] for row in self.values] for i in range(self.shape[1])
            ]
        )

    def __repr__(self):
        return f"Vector({self.values})"

    def __str__(self):
        return self.__repr__()

    def __add__(self, v):
        if type(v) == list:
            v = Vector(v)
        elif type(v) != Vector:
            raise NotImplementedError(f"Cannot add '{type(v).__name__}' object to '{type(self).__name__}' object")
        if self.shape != v.shape:
            raise ValueError("Vectors does not have the same shape")
        return Vector(
                [
                    [x1 + x2 for x1, x2 in zip(row1, row2)]
                    for row1, row2 in zip(self.values, v.values)
                ]
        )


    def __radd__(self, v):
        return self.__add__(v)

    def __mul__(self, s):
        if type(s) not in (int, float):
            raise NotImplementedError(f"'{type(s).__name__}' is not a scalar")
        return Vector(
                [
                    [x * s for x in row]
                    for row in self.values
                ]
        )

    def __rmul__(self, v):
        return self.__mul__(v)

    def __sub__(self, v):
        if type(v) == list:
            v = Vector(v)
        elif type(v) != Vector:
            raise NotImplementedError(f"Cannot substract '{type(v).__name__}' object to '{type(self).__name__}' object")
        if self.shape != v.shape:
            raise ValueError("Vectors does not have the same shape")
        return Vector(
                [
                    [x1 - x2 for x1, x2 in zip(row1, row2)]
                    for row1, row2 in zip(self.values, v.values)
                ]
        )

    def __rsub__(self, v):
        return self.__sub__(v).__mul__(-1)

    def __truediv__(self, s):
        if type(s) not in (int, float):
            raise NotImplementedError(f"'{type(s).__name__}' is not a scalar")
        if s == 0:
            raise ZeroDivisionError
        return Vector(
                [
                    [x / s for x in row]
                    for row in self.values
                ]
        )

    def __rtruediv__(self, v):
        raise NotImplementedError(f"Division of a scalar by a Vector is not defined here.")


