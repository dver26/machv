import numpy as np
from tabulate import tabulate

# formato: [nombre, tipo1, tipo2, hp, attack, defense, sp_atk, sp_def, speed, legendary]

class Dataset:
    def __init__(self, X, y, names, nameY):
        self.X = np.array(X)
        self.y = np.array(y)
        if len(names) != self.X.shape[1]:
            raise ValueError("Names length and the number of columns of the table aren't the same.")
        else:
            self.names = names

        self.nameY = nameY

    def __len__(self):
        return self.X.shape[0]

    def __str__(self):
        y = self.y
        y = y.reshape(-1, 1)
        return tabulate(np.concatenate((self.X, y), axis = 1), headers=self.names + [self.nameY],  tablefmt="fancy_grid")

    def n_attr(self):
        return self.X.shape[1]
        

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

    @property
    def names(self):
        return self._names

    @names.setter
    def names(self, value):
        self._names = value

    @property
    def nameY(self):
        return self._nameY

    @nameY.setter
    def nameY(self, value):
        self._nameY = value
