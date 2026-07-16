import numpy as np
from matplotlib import pyplot
import PIL

class ImageProcessor:

    @staticmethod
    def load(path: str) -> np.ndarray | None:
        try:
            img = np.asarray(PIL.Image.open(path))
            print(f"Loading image of dimmensions {img.shape[0]} x {img.shape[1]}")
        except FileNotFoundError:
            print(f"Error: {path} not found")
            return None
        except PIL.UnidentifiedImageError:
            print(f"Error: {path} is not a valid image")
            return None
        return img

    @staticmethod
    def display(array: np.ndarray) -> None:
        pyplot.imshow(array)
        pyplot.show()