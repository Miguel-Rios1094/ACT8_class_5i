print("clases version 2 el constructor")
class Perro:
    # funcion constructor
    def __init__(self,color,edad):
        self.color=color
        self.edad=edad
    # funciones creadas por el usuario
    def morder(self):
        print("El perro me mordio!")
        
    def chatperro(self,mensaje):
        print(f"Chat perro: {mensaje}")
    
    def chatperra(self,mensajep):
        print(f"Chat perra: {mensajep}")
        
    def datos(self):
        print(f"color {self.color} edad {self.edad}")
        
# crear el objeto
chihuas=Perro("Negro",2)
#llamadas a funciones
chihuas.datos()
chihuas.morder()
chihuas.chatperro("Hola canina")
chihuas.chatperra("Hola boby")

