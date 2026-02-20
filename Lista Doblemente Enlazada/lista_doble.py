from graphviz import Digraph

class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return f"{self.nombre} {self.apellido}\n{self.carnet}"


class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None

    # Insertar al principio
    def insertar_al_principio(self, nombre, apellido, carnet):
        nuevo = Nodo(nombre, apellido, carnet)

        if self.cabeza is not None:
            self.cabeza.anterior = nuevo
            nuevo.siguiente = self.cabeza

        self.cabeza = nuevo
        self.generar_grafica()

    # Insertar al final
    def insertar_al_final(self, nombre, apellido, carnet):
        nuevo = Nodo(nombre, apellido, carnet)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente

            actual.siguiente = nuevo
            nuevo.anterior = actual

        self.generar_grafica()

    # Eliminar por carnet
    def eliminar_por_valor(self, carnet):
        actual = self.cabeza

        while actual:
            if actual.carnet == carnet:
                # Si es el primero
                if actual.anterior is None:
                    self.cabeza = actual.siguiente
                    if self.cabeza:
                        self.cabeza.anterior = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    if actual.siguiente:
                        actual.siguiente.anterior = actual.anterior

                print("Nodo eliminado correctamente.")
                self.generar_grafica()
                return

            actual = actual.siguiente

        print("No se encontró el carnet.")

    # Mostrar lista
    def mostrar_lista(self):
        actual = self.cabeza
        resultado = "None <- "

        while actual:
            resultado += f"[{actual.nombre} {actual.apellido} - {actual.carnet}] <-> "
            actual = actual.siguiente

        resultado += "None"
        print(resultado)

    # Crear gráfica con Graphviz
    def generar_grafica(self):
        dot = Digraph(format="png")
        dot.attr(rankdir="LR")

        actual = self.cabeza
        i = 0
        anterior_id = None

        while actual:
            node_id = f"N{i}"
            dot.node(node_id, str(actual))

            if anterior_id:
                dot.edge(anterior_id, node_id)
                dot.edge(node_id, anterior_id)

            anterior_id = node_id
            actual = actual.siguiente
            i += 1

        dot.render("lista_doble", view=False)
        print("Imagen actualizada: lista_doble.png")


# ==============================
#        INTERFAZ


def menu():
    lista = ListaDoblementeEnlazada()

    while True:
        print("\n===== MENÚ =====")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Eliminar por carnet")
        print("4. Mostrar lista")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")
            lista.insertar_al_principio(nombre, apellido, carnet)

        elif opcion == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")
            lista.insertar_al_final(nombre, apellido, carnet)

        elif opcion == "3":
            carnet = input("Carnet a eliminar: ")
            lista.eliminar_por_valor(carnet)

        elif opcion == "4":
            lista.mostrar_lista()

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()




    
