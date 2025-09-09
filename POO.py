#Autor: Miguel Silva
#Manejo de creacion de clases, atributos y metodos

#Creacion mascota
class Mascota:
    def __init__(self, color, raza, peso, nombre):
        self.color=color
        self.raza=raza
        self.peso=peso
        self.nombre=nombre

    def __str__(self):
        str_color=f"-------------\nColor: {self.color}\n"
        str_raza=f"Raza: {self.raza}\n"
        str_peso=f"Peso: {self.peso}\n"
        str_nombre=f"Nombre: {self.nombre}\n-------------\n"
        return str_color + str_raza + str_peso + str_nombre

#Creacion clase perro
class Perro(Mascota):
    def __init__(self, color, raza, peso, nombre):
        super().__init__(color, raza, peso, nombre)
    
    def __str__(self):
        return super().__str__()

    def ladrar(self):
        print("Guau!\n")

#Creacion clase gato
class Gato(Mascota):
    def __init__(self, color, raza, peso, nombre):
        super().__init__(color, raza, peso, nombre)
    
    def __str__(self):
        return super().__str__()
    
    def maullar(self):
        print("Miau!\n")

#Funcion main()
def main():
    color_perro=input("Ingrese el color de su perro: ")
    raza_perro=input("Ingrese la raza de su perro: ")
    peso_perro=input("Ingrese el peso de su perro: ")
    nombre_perro=input("Ingrese el nombre de su perro: ")
    mi_perro= Perro(color_perro,raza_perro,peso_perro,nombre_perro)
    print(mi_perro)
    mi_perro.ladrar()

    color_gato=input("Ingrese el color de su gato: ")
    raza_gato=input("Ingrese la raza de su gato: ")
    peso_gato=input("Ingrese el peso de su gato: ")
    nombre_gato=input("Ingrese el nombre de su gato: ")
    mi_gato=Gato(color_gato,raza_gato,peso_gato,nombre_gato)
    print(mi_gato)
    mi_gato.maullar()

#Ejecutar la funcion main()
if __name__=="__main__":
    main()