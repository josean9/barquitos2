
from venv import *
from juego import ORIENTACIONES
from juego import HORIZONTAL

from clases import Case
from clases import Conventions
from random import choice
from itertools import product, repeat

instances = []
casillas_ocupadas = set()
class Barco:
    def __init__(self, longitud, orientacion=choice(ORIENTACIONES), tocado=False, hundido=False):
            self.longitud = longitud
            self.orientacion = orientacion
            self.tocado = tocado
            self.hundido = hundido
            

            # performance / legibilidad:
            num_lineas = Conventions.tablero_num_lineas
            num_columnas = Conventions.tablero_num_columnas
            num2l = Conventions.generar_num_linea
            num2c = Conventions.generar_num_columna

            if self.orientacion == HORIZONTAL:
                rang = choice(range(num_lineas))
                primero = choice(range(num_columnas + 1 - longitud))
                letra = num2l(rang)
                cifras = [num2c(x) for x in range(primero, primero + longitud)]
                self.casillas = {Case.instances[l + c]
                                for l, c in product(repeat(letra, longitud), cifras)}
            else:
                rang = choice(range(num_columnas))
                primero = choice(range(num_lineas + 1 - longitud))
                cifra = num2c(rang)
                letras = [num2l(x) for x in range(primero, primero + longitud)]
                    # Crear el barco
                self.casillas = {Case.instances[l + c]
                    for l, c in product(letras, repeat(cifra, longitud))}

            for existente in instances:
                if self.casillas.intersection(existente.casillas):
                    break  # break relativo al "for existente in barcos:"
                else:
                    # Agregar el barco en el contenedor de barcos
                    instances.append(self)
                    # Informar la casilla que contiene un barco.
                    for casilla in self.casillas:
                        casilla.barco = self
                    # Agregar estas casillas a las casillas ocupadas :
                    casillas_ocupadas |= self.casillas
                    break 
            else:
                # Si no se rompió el bucle, no se ha podido crear el barco
                raise ValueError("No se pudo crear el barco")
@classmethod
def generar_barcos():
    """Genera todos los barcos del tablero"""
    for longitud in Conventions.LONGITUDES_BARCOS:
        Barco(longitud)
"""@classmethod
def generar_barcos():
    
    conjuntoDeBarcos = {"barco1":[], "barco2":[], "barco3":[], "barco4":[], "barco5":[], "barco6":[]}
    contador=0
    for longitud in Conventions.LONGITUDES_BARCOS:
        conjuntoDeBarcos[contador] = longitud
        contador+=1"""