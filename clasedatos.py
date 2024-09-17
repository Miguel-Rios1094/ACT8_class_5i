class Informaciion:
    def mi_lista(self):
        lista_Nomperros=["boby","Dollar","fany"]
        for x in lista_Nomperros:
            print(x)
    
    def mi_tupla(self):
        Raza = ("Chihuahua", "Bulldog", "Pug")
        for z in Raza:
            print(z)
    def mi_diccionario(self):
        GenAnim = {
            "boby": "masculino",
            "fany": "Femenino",
            "Dollar": "Masculino"
        }
        for a, c in GenAnim.items():
            print(a, c)
    def mi_conjunto(self):
        Colores = {"Azul", "Gris", "Rojo"}
        for b in Colores:
            print(b)
        
# Creando el objeto

datos=Informaciion()
print("-///////////////-Listado de nombre de perros-///////////////-")
datos.mi_lista()
print("-///////////////-Tupla de raza de perros-///////////////-")
datos.mi_tupla()
print("-///////////////-Diccionario de Genero de perros-///////////////-")
datos.mi_diccionario()
print("-///////////////-Conjunto de de perros-///////////////-")
datos.mi_conjunto()