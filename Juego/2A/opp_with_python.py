class Personaje:
 
    def __init__(self, nombre, fuerza, inteligencia, vida, defensa):
        self._nombre = nombre
        self._fuerza = fuerza
        self._inteligencia = inteligencia
        self._vida = vida
        self._defensa = defensa
       
    def atributos(self):
        print(f"Nombre: {self._nombre}")
        print(f"Fuerza: {self._fuerza}")
        print(f"Inteligencia: {self._inteligencia}")
        print(f"Vida: {self._vida}")
        print(f"Defensa: {self._defensa}")
       
    def Nivel(self, fuerza, inteligencia, vida, defensa):
        self._fuerza += fuerza
        self._inteligencia += inteligencia
        self._vida += vida
        self._defensa += defensa
   
    def esta_vivo(self):
        return self._vida > 0
   
    def _morir(self):
        self._vida = 0
        print(f"Tu personaje {self._nombre} ha muerto")
       
    def dañar(self, enemigo):
        return self._fuerza - enemigo._defensa if self._fuerza > enemigo._defensa else 0
   
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo._vida = enemigo._vida - daño
        print(self._nombre, "ha realizado", daño, "puntos de daño a", enemigo._nombre)
        print("Vida de ", enemigo._nombre, "es", enemigo._vida)

    def get_fuerza(self):
        return self._fuerza
    
    def set_fuerza(self,fuerza):
        if fuerza < 0:
            print("Error, ha puesto un valor negativo")
        self._fuerza = fuerza


#Variable del constructor  de la clase
mi_personaje = Personaje("Pipito", 8000, 90, 50, 100)
mi_enemigo = Personaje("Enemigo", 60, 90, 100, 100)
print(mi_personaje.dañar(mi_enemigo))

#print(mi_personaje.esta_vivo())
mi_personaje.atributos()
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()

#pruebas 

#mi_personaje.atacar(mi_enemigo)
#print(mi_personaje.get_fuerza())
#mi_personaje.set_fuerza(-100)
#print(mi_personaje.get_fuerza())
mi_personaje._Personaje_fuerza = 10
mi_personaje.atributos()