class Animal:
    def comer(self):
        print("El animal esta comiendo")

class Ave(Animal):
    def volar(self):
        print("El animal está volando")

class Mamífero(Animal):
    def amamantar (self):
        print("El animal esta amamantando")
        
class Perro(Mamífero,Ave):
    pass

perro = Perro()

perro.comer()

perro.amamantar()                 