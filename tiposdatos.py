print("clases V2 Ariel Rodriguez")
#zona de clase
class Datos:
    #el constructor funcion
    def __init__(self,estatura,peso):
        self.estatura=estatura
        self.peso=peso
    def mostrar_datos(self):
        print(f"estatura : {self.estatura} mts peso : {self.peso} kg")
    def mi_lista(self):
        albums=["blond","roy","suave pendiente"]
        print(albums)
        for alb in albums:
            print(alb)
        
#creacion de objetos info
info=Datos(1.75,70.5)

#utilizando el obj
info.mostrar_datos()
print(" lista de los mejores albums Rodriguez Ariel")
info.mi_lista()
#tuplas
print("Ejemplo de tuplas")
artistas=("frank ocean","zoe","Simon Campusano")
print(artistas)
# diccionario
print("Esto es un ejemplo de diccionario")
audifonos = {
"marca": "apple",
"modelo": "version 1.9",
"año": 2024
}
print(audifonos)