class Forma():

    def area(self):
        pass


class Quadrado(Forma):
    
    def __init__(self, lado):
       self.lado = lado
    
    def area(self):
        return self.lado ** 2
    

class Circulo(Forma):
    
    def __init__(self, raio):
        self.raio = raio

    def area(self, raio):
        return 3.14 * raio ** 2
    

quadrado = Quadrado(5)
area_quadrado = quadrado.area()
print(area_quadrado)