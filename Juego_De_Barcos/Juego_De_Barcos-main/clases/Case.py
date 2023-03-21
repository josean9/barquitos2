from itertools import product

from juego import CASO_NO_JUGADO, CASO_AGUA, CASO_TOCADO
from clases import Barco, Conventions, Case, Tablero



instances = {}
jugadas = set()

def __init__(self, x, y):
  # Adición de las coordenadas
  self.x = x
  self.y = y
  # Queremos poder acceder a una casilla a partir de sus coordenadas
  instances[x, y] = self
  
  # Generación del nombre de la casilla
  self._generar_nombre()
  # Queremos poder acceder a una casilla a partir de su nombre
  instances[self.nombre] = self
  
  # Evolución de la casilla
  self.jugada = False
  self.barco = None  # No toca a un barco de momento.

def _generar_nombre(self):
  """Este método puede ser sobrecargado fácilmente"""
  self.nombre = chr(self.x + Conventions.CODIGO_PRIMERA_LETRA) + str(self.y)

def jugar(self):
  """Describe qué pasa cuando jugamos una casilla"""
  self.jugada = True
  self.jugadas.add(self)
  
  if self.barco is not None:
      if len(self.casillas - self.casillas_jugadas) == 0:
          print("Hundido !!")
      else:
          print("Tocado !")
  else:
      print("Agua !")

@classmethod
def generar_casillas():
  """Genera todas las casillas del tablero"""
  for x, y in product(range(Conventions.LONGITUD_TABLERO),
                      range(Conventions.LONGITUD_TABLERO)):
      Case(x, y)

def __str__(self):
  """Sobrecarga del método de transformación en cadena"""
  if not self.jugada:
      return CASO_NO_JUGADO
  elif self.barco is None:
      return CASO_AGUA
  return CASO_TOCADO
