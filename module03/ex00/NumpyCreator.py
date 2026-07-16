import numpy as np

class NumpyCreator:

    def __init__(self):
        pass
    def from_list(self, lst: list) -> np.ndarray:

        """Takes a list or nested lists and returns its corresponding Numpy array"""
        return np.array(lst)

    def from_tuple(self, tpl: tuple) -> np.ndarray:
        """Takes a tuple or nested tuples and returns its corresponding Numpy array."""
        return np.array(tpl)
    
    def from_iterable(self, itr):
        """Takes an iterable and returns an array which contains all of its elements."""
        return np.fromiter(itr, float)

    def from_shape(self, shape: tuple, value: float=0.0) -> np.ndarray:
        """
            Returns an array filled with the same value.
            The first argument is a tuple which specifies the shape of the array, and the second
            argument specifies the value of the elements. This value must be 0 by default.
            """
        return np.full(shape, value)

    def random(self, shape: tuple) -> np.ndarray:
        """
            Returns an array filled with random values. It takes as an
            argument a tuple which specifies the shape of the array.
        """
        return np.random.default_rng().random(shape)

    def identity(self, n: int) -> np.ndarray:
        """
            Returns an array representing the identity matrix of size n.
        """
        return np.identity(n)