from colored import fg, attr

class Tablero:
    colores={
        "rojo": fg("red"),
        "azul": fg("blue"),
        "verde": fg("green"),
        "amarillo": fg("yellow")
    }
    
    def __init__(self):
        self.color=[]
        self.turnos=[]
    
    
    def definir_color(self, color):
        self.color = color #Lista que contiene los colores
    
    
        