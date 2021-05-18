#ejemplo de clases ampliacion de temario

class Persona: #clase persona

    #atributos de la clase
    nombre = None 
    apellido = None
    edad = None

    #constructor con los atributos a rellenar
    def __init__(self, nombre, apellido, edad): 
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    #getters and setters
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getApellido(self):
        return self.apellido

    def setApellido(self, apellido):
        self.apellido = apellido

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    #metodos dentro de la clase
    def mostrarInfo(self):
        print('Nombre: ', self.nombre, '\nApellido: ', self.apellido, '\nEdad: ', self.edad)
    
