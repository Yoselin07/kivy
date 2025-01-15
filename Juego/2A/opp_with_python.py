class Personaje:
    #Atributos de la clase
    nombre = 'default'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0 
#Variable del constructor vacío de la clase 
mi_personaje = Personaje()
#Modificando los valores de los atributos
mi_personaje.nombre = 'queso'
mi_personaje.fuerza = 9001
print("El nombre del personaje es ",mi_personaje.nombre)
print("La fuerza del personaje es ",mi_personaje.fuerza)
