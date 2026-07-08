import numpy as np

class Dataset:
    def __init__(self, X, y, names):
        self.X = np.array(X)
        self.y = np.array(y)
        if len(names) != self.X.shape[1]:
            raise ValueError("Names length and the number of columns of the table aren't the same.")
        else:
            self.names = names

    @property
    def X(self):
        """Geter de la taula de X"""
        return self._X

    @X.setter
    def X(self, new_X):
        self._X = new_X

    @property
    def y(self):
        """The  property."""
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value 


