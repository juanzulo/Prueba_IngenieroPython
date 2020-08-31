"""
Autor: Juan David Zuluaga Lopez
"""
#librerias
from random import randint

#clase para el tablero de ajedrez
class tableros:
    data = []
    
    def __init__(self):
        self.data = [[0,0,0,0,0,0,0,0]
                    ,[0,0,0,0,0,0,0,0]
                    ,[0,0,0,0,0,0,0,0]
                    ,[0,0,0,0,0,0,0,0]
                    ,[0,0,0,0,0,0,0,0]
                    ,[0,0,0,0,0,0,0,0]
                    ,[0,0,0,0,0,0,0,0]
                    ,[0,0,0,0,0,0,0,0]]
    
    def mostrar_tablero(self):
        print("[" + " ".join(map(str,self.data)).replace(",","").replace("] [","]\n[") + "]")
    
#clases para la piezas de ajedrez
class piezas:
    posx= randint(0,7)
    posy= randint(0,7)

#el movimiento del peon se expresara hacia arriba
class peon(piezas):
    def calcular_movimientos(self, tablero):
        #posiion imposible para el peon, al tener valor aleatorio se reescribe
        #solo para el reto dado otro caso seria un manejo de error
        if self.posy == 7:
            self.posy=6
        #posicionamos pieza
        tablero.data[self.posy][self.posx] = 8
        #avanza 1 si puede
        if self.posy > 0:
            tablero.data[self.posy - 1][self.posx] = 1
        #avanza 2 si esta en posicion inicial
        if self.posy == 6:
            tablero.data[self.posy - 2][self.posx] = 1
        
        #imprimimos movimientos
        print("Peón")
        tablero.mostrar_tablero()
        
    
class torre(piezas):
    def calcular_movimientos(self, tablero):
        #posicionamos pieza
        tablero.data[self.posy][self.posx] = 8
        #iteramos por los laterales para amrcar movimiento
        for x in range(8):
            #marcacion vertical
            if x != self.posy:
                tablero.data[x][self.posx] = 1
            #marcacion horizontal
            if x != self.posx:
                tablero.data[self.posy][x] = 1
        
        #imprimimos movimientos
        print("Torre")
        tablero.mostrar_tablero()
        
class caballo(piezas):
    def calcular_movimientos(self, tablero):
        #posicionamos pieza
        tablero.data[self.posy][self.posx] = 8
        #marca movimiento hacia abajo si puede
        if self.posy + 2 < 8:
            if self.posx == 0:
                tablero.data[self.posy + 2][self.posx + 1] = 1
            elif self.posx == 7:
                tablero.data[self.posy + 2][self.posx - 1] = 1
            else:
                tablero.data[self.posy + 2][self.posx + 1] = 1
                tablero.data[self.posy + 2][self.posx - 1] = 1
        #marca movimiento hacia arriba si puede
        if self.posy - 2 >= 0:
            if self.posx == 0:
                tablero.data[self.posy - 2][self.posx + 1] = 1
            elif self.posx == 7:
                tablero.data[self.posy - 2][self.posx - 1] = 1
            else:
                tablero.data[self.posy - 2][self.posx + 1] = 1
                tablero.data[self.posy - 2][self.posx - 1] = 1
        #marca movimiento hacia la derecha si puede
        if self.posx + 2 < 8:
            if self.posy == 0:
                tablero.data[self.posy + 1][self.posx + 2] = 1
            elif self.posy == 7:
                tablero.data[self.posy - 1][self.posx + 2] = 1
            else:
                tablero.data[self.posy + 1][self.posx + 2] = 1
                tablero.data[self.posy - 1][self.posx + 2] = 1
        #marca movimiento hacia la izquierda si puede
        if self.posx - 2 >= 0:
            if self.posy == 0:
                tablero.data[self.posy + 1][self.posx - 2] = 1
            elif self.posy == 7:
                tablero.data[self.posy - 1][self.posx - 2] = 1
            else:
                tablero.data[self.posy + 1][self.posx - 2] = 1
                tablero.data[self.posy - 1][self.posx - 2] = 1
        
        #imprimimos movimientos
        print("Caballo")
        tablero.mostrar_tablero()
    

class alfil(piezas):
    def calcular_movimientos(self, tablero):
        #posicionamos pieza
        tablero.data[self.posy][self.posx] = 8
        #iteramos por las diagonales para marcar movimiento
        for x in range(8):
            #diagolanl secundaria
            if x != self.posy and self.posx + (self.posy - x) >= 0 and self.posx + (self.posy - x) < 8:
                tablero.data[x][self.posx + (self.posy - x)] = 1
            #diagonal principal
            if x != self.posy and self.posx + (x - self.posy) >= 0 and self.posx + (x - self.posy) < 8:
                tablero.data[x][self.posx + (x - self.posy)] = 1
        
        #imprimimos movimientos
        print("Alfil")
        tablero.mostrar_tablero()

class reina(piezas):
    def calcular_movimientos(self, tablero):
        #posicionamos pieza
        tablero.data[self.posy][self.posx] = 8
        #iteramos por los laterales para marcar movimiento
        for x in range(8):
            #marcacion vertical
            if x != self.posy:
                tablero.data[x][self.posx] = 1
            #marcacion horizontal
            if x != self.posx:
                tablero.data[self.posy][x] = 1
        #iteramos por las diagonales para marcar movimiento
        for x in range(8):
            #diagolanl secundaria
            if x != self.posy and self.posx + (self.posy - x) >= 0 and self.posx + (self.posy - x) < 8:
                tablero.data[x][self.posx + (self.posy - x)] = 1
            #diagonal principal
            if x != self.posy and self.posx + (x - self.posy) >= 0 and self.posx + (x - self.posy) < 8:
                tablero.data[x][self.posx + (x - self.posy)] = 1
        
        #imprimimos movimientos
        print("Reina")
        tablero.mostrar_tablero()

class rey(piezas):
    def calcular_movimientos(self, tablero):
        #posicionamos pieza
        tablero.data[self.posy][self.posx] = 8
        #movimiento hacia abajo
        if self.posy + 1 < 8:
            tablero.data[self.posy + 1][self.posx] = 1
        #movimiento hacia arriba
        if self.posy - 1 >= 0:
            tablero.data[self.posy - 1][self.posx] = 1
        #movimiento hacia la derecha
        if self.posx + 1 < 8:
            tablero.data[self.posy][self.posx + 1] = 1
        #movimiento hacia la izquierda
        if self.posx - 1 >= 0:
            tablero.data[self.posy][self.posx - 1] = 1
        
        #imprimimos movimientos
        print("Rey")
        tablero.mostrar_tablero()
    
#programa principal
if __name__ == "__main__":
    peon().calcular_movimientos(tableros())
    torre().calcular_movimientos(tableros())
    caballo().calcular_movimientos(tableros())
    alfil().calcular_movimientos(tableros())
    reina().calcular_movimientos(tableros())
    rey().calcular_movimientos(tableros())