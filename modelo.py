import math

class ModeloPlanta:

    "Funcion de logistica"
    
    @staticmethod
    def logistica(P0, Pmax, r, t):
        return Pmax / (1 + ((Pmax - P0) / P0) * math.exp(-r * t))
