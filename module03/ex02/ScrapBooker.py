import numpy as np

class ScrapBooker:
    """Class for image manipulation operations using numpy arrays."""

    def crop(self, array: np.ndarray, dim: tuple[int, int], position=(0, 0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.

        Args:
        -----
            array: numpy.ndarray
            dim: tuple of 2 integers.
            position: tuple of 2 integers.

        Returns:
        --------
            new_arr: the cropped numpy.ndarray.
            None: (if the combination of parameters is not possible).

        Raises:
        -------
            This function should not raise any Exception.
        """
        if any(d < 0 for d in dim) or any(p < 0 for p in position):
            return None
        return array[position[0]:dim[0], position[1]:dim[1]:, :]


    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis
        (0: vertical, 1: horizontal).

        Args:
        -----
            array: numpy.ndarray.
            n: non null positive integer lower than the number of row/column
               of the array (depending of axis value).
            axis: positive non null integer.

        Returns:
        --------
            new_arr: thinned numpy.ndarray.
            None: (if the combination of parameters is not possible).

        Raises:
        -------
            This function should not raise any Exception.
        """
        pass

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.

        Args:
        -----
            array: numpy.ndarray.
            n: positive non null integer.
            axis: integer of value 0 or 1.

        Returns:
        --------
            new_arr: juxtaposed numpy.ndarray.
            None: (if the combination of parameters is not possible).

        Raises:
        -------
            This function should not raise any Exception.
        """
        pass

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument
        specifies the number of repetition along each dimensions.

        Args:
        -----
            array: numpy.ndarray.
            dim: tuple of 2 integers.

        Returns:
        --------
            new_arr: mosaic numpy.ndarray.
            None: (combination of parameters not compatible).

        Raises:
        -------
            This function should not raise any Exception.
        """
        pass
