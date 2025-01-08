import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
 
class Muñeco(Widget):
    def __init__(self, **kwargs):
        super(Muñeco, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (50, 50)
        self.pos = (100, 100)
        self.velocidad = 5
        self.nivel = 1
        self.intentos = 3
        self.gano = False
 
        self.bind(pos=self.actualizar_posicion)
 
    def actualizar_posicion(self, instance, pos):
        if pos[0] < 0 or pos[0] > self.parent.width - self.width:
            self.velocidad = -self.velocidad
        if pos[1] < 0 or pos[1] > self.parent.height - self.height:
            self.velocidad = -self.velocidad
 
    def mover(self):
        self.pos = (self.pos[0] + self.velocidad, self.pos[1])
 
    def verificar_nivel(self):
        if self.nivel == 1 and self.pos[0] > self.parent.width / 2:
            self.nivel = 2
            self.velocidad += 2
        elif self.nivel == 2 and self.pos[0] > self.parent.width / 2:
            self.nivel = 3
            self.velocidad += 2
        elif self.nivel == 3 and self.pos[0] > self.parent.width / 2:
            self.nivel = 4
            self.velocidad += 2
        elif self.nivel == 4 and self.pos[0] > self.parent.width / 2:
            self.gano = True
 
    def verificar_perdida(self):
        if self.pos[0] < 0 or self.pos[0] > self.parent.width - self.width:
            self.intentos -= 1
            if self.intentos == 0:
                self.gano = False
 
class Juego(App):
    def build(self):
        self.root = Widget()
        self.muñeco = Muñeco()
        self.root.add_widget(self.muñeco)
 
        Clock.schedule_interval(self.muñeco.mover, 1.0 / 60.0)
        Clock.schedule_interval(self.muñeco.verificar_nivel, 1.0)
        Clock.schedule_interval(self.muñeco.verificar_perdida, 1.0)
 
        return self.root
 
if __name__ == '__main__':
    Juego().run()
