import numpy as np
from matplotlib import image

class ImageProcessor:

    @staticmethod
    def load(path: str) -> np.ndarray:
        try:
            img = image.imread(path)
            print(f"Loading image of dimmensions {img.shape[0]} x {img.shape[1]}")
        except FileNotFoundError:
            print(f"{path} not found")
            return None
        except 
        return img

    @staticmethod
    def display(array: np.ndarray) -> None:
        pass