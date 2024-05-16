class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

class ListaCanciones:
    def __init__(self):
        self.cabeza = None

    def agregar(self, nombre):
        nuevo = Nodo(nombre)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def quitar(self, nombre):
        if not self.cabeza:
            return
        if self.cabeza.nombre == nombre:
            self.cabeza = self.cabeza.siguiente
            return
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.nombre == nombre:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente

    def ver(self, indice):
        if indice < 0:
            print("No puedes ver esa canción.")
            return
        actual = self.cabeza
        for _ in range(indice):
            if actual:
                actual = actual.siguiente
            else:
                print("No puedes ver esa canción.")
                return
        print(actual.nombre)

    def esta_vacia(self):
        return self.cabeza is None

    def cuantas(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.nombre)
            actual = actual.siguiente

def menu():
    while True:
        print("""
        ¡Hola! ¿Qué quieres hacer con tu lista de música?

        1. Agregar una canción
        2. Quitar una canción
        3. Ver una canción
        4. Ver cuántas canciones hay
        5. Mostrar todas las canciones
        6. Salir
        """)
        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            agregar(lista)
        elif opcion == "2":
            quitar(lista)
        elif opcion == "3":
            indice = int(input("¿Qué canción quieres ver? (Ingresa su número): "))
            ver(lista, indice)
        elif opcion == "4":
            canciones = cuantas(lista)
            print(f"¡Tienes {canciones} canciones en tu lista!")
        elif opcion == "5":
            mostrar(lista)
        elif opcion == "6":
            print("¡Adiós!")
            break
        else:
            print("¡Opción inválida! Intenta de nuevo.")

def agregar(lista):
    nombre = input("¿Cómo se llama la canción que quieres agregar? ")
    lista.agregar(nombre)
    print(f"¡La canción '{nombre}' se agregó a tu lista!")

def quitar(lista):
    nombre = input("¿Qué canción quieres quitar? ")
    lista.quitar(nombre)
    print(f"¡La canción '{nombre}' se quitó de tu lista!")

def ver(lista, indice):
    lista.ver(indice)

def cuantas(lista):
    return lista.cuantas()

def mostrar(lista):
    if lista.esta_vacia():
        print("¡Tu lista de música está vacía!")
    else:
        print("¡Aquí están tus canciones!")
        lista.mostrar()

# ¡Inicia la aplicación!
lista = ListaCanciones()
menu()