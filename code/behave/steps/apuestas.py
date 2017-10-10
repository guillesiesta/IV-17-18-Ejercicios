from behave import *


class Apuesta:
    """
    Clase Apuesta.
    """

    def __init__(self, loc="", vis="", fec="", r=["", "-", ""]):
        self.local = loc
        self.visitante = vis
        self.fecha = fec
        self.resultado = r

    def Apostar(self, local, visitante, fecha, gol_local, gol_visitante):

        if type(local) is not str:
            return False
        else:
            self.local = local

        if type(visitante) is not str:
            return False
        else:
            self.visitante = visitante

        if type(fecha) is not str:
            return False
        else:
            self.fecha = fecha

        if type(gol_local) is not str:
            return False
        else:
            self.resultado[0] = gol_local

        if type(gol_visitante) is not str:
            return False
        else:
            self.resultado[2] = gol_visitante

        return True

    def MostrarApuesta(self):
        print (" Equipo local: ", self.local, " Equipo visitante: ", self.visitante, "Fecha: ", self.fecha, " Resultado: ")
        i = 0
        size = len(self.resultado)
        while i < size:
            print (self.resultado[i])
            i += 1

        return True
