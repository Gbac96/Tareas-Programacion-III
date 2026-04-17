import csv
from graphviz import Digraph

# =========================
# Nodo AVL
# =========================
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1


# =========================
# Árbol AVL
# =========================
class AVL:
    def __init__(self):
        self.raiz = None

    def altura(self, nodo):
        return nodo.altura if nodo else 0

    def balance(self, nodo):
        return self.altura(nodo.izq) - self.altura(nodo.der) if nodo else 0

    def rotar_derecha(self, y):
        x = y.izq
        T2 = x.der

        x.der = y
        y.izq = T2

        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))
        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))

        return x

    def rotar_izquierda(self, x):
        y = x.der
        T2 = y.izq

        y.izq = x
        x.der = T2

        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))
        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))

        return y

    # =========================
    # INSERTAR
    def insertar(self, nodo, valor):
        if not nodo:
            return Nodo(valor)

        if valor < nodo.valor:
            nodo.izq = self.insertar(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self.insertar(nodo.der, valor)
        else:
            return nodo

        nodo.altura = 1 + max(self.altura(nodo.izq), self.altura(nodo.der))

        balance = self.balance(nodo)

        # Rotaciones
        # Izquierda Izquierda
        if balance > 1 and valor < nodo.izq.valor:
            return self.rotar_derecha(nodo)

        # Derecha Derecha
        if balance < -1 and valor > nodo.der.valor:
            return self.rotar_izquierda(nodo)

        # Izquierda Derecha
        if balance > 1 and valor > nodo.izq.valor:
            nodo.izq = self.rotar_izquierda(nodo.izq)
            return self.rotar_derecha(nodo)

        # Derecha Izquierda
        if balance < -1 and valor < nodo.der.valor:
            nodo.der = self.rotar_derecha(nodo.der)
            return self.rotar_izquierda(nodo)

        return nodo

    def buscar(self, nodo, valor):
        if not nodo:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self.buscar(nodo.izq, valor)
        else:
            return self.buscar(nodo.der, valor)


    # OBTENER MÍNIMO

    def minimo(self, nodo):
        if nodo is None or nodo.izq is None:
            return nodo
        return self.minimo(nodo.izq)


    # ELIMINAR

    def eliminar(self, nodo, valor):
        if not nodo:
            return nodo

        if valor < nodo.valor:
            nodo.izq = self.eliminar(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self.eliminar(nodo.der, valor)
        else:
            if not nodo.izq:
                return nodo.der
            elif not nodo.der:
                return nodo.izq

            temp = self.minimo(nodo.der)
            nodo.valor = temp.valor
            nodo.der = self.eliminar(nodo.der, temp.valor)

        if not nodo:
            return nodo

        nodo.altura = 1 + max(self.altura(nodo.izq), self.altura(nodo.der))
        balance = self.balance(nodo)

        # Rotaciones
        if balance > 1 and self.balance(nodo.izq) >= 0:
            return self.rotar_derecha(nodo)

        if balance > 1 and self.balance(nodo.izq) < 0:
            nodo.izq = self.rotar_izquierda(nodo.izq)
            return self.rotar_derecha(nodo)

        if balance < -1 and self.balance(nodo.der) <= 0:
            return self.rotar_izquierda(nodo)

        if balance < -1 and self.balance(nodo.der) > 0:
            nodo.der = self.rotar_derecha(nodo.der)
            return self.rotar_izquierda(nodo)

        return nodo


    def graficar(self):
        dot = Digraph()

        def recorrer(nodo):
            if nodo:
                dot.node(str(nodo.valor))
                if nodo.izq:
                    dot.edge(str(nodo.valor), str(nodo.izq.valor))
                    recorrer(nodo.izq)
                if nodo.der:
                    dot.edge(str(nodo.valor), str(nodo.der.valor))
                    recorrer(nodo.der)

        recorrer(self.raiz)
        dot.render("arbol_avl", view=True)



# CARGAR CSV

def cargar_csv(avl, archivo):
    try:
        with open(archivo, newline='') as f:
            reader = csv.reader(f)
            for fila in reader:
                for valor in fila:
                    avl.raiz = avl.insertar(avl.raiz, int(valor))
        print("Datos cargados correctamente.")
    except Exception as e:
        print("Error al cargar archivo:", e)

def menu():
    avl = AVL()

    while True:
        print("\n=== ÁRBOL UMG ===")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Cargar desde CSV")
        print("5. Visualizar (Graphviz)")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            valor = int(input("Ingrese número: "))
            avl.raiz = avl.insertar(avl.raiz, valor)

        elif opcion == "2":
            valor = int(input("Buscar número: "))
            print("Encontrado" if avl.buscar(avl.raiz, valor) else "No encontrado")

        elif opcion == "3":
            valor = int(input("Eliminar número: "))
            avl.raiz = avl.eliminar(avl.raiz, valor)

        elif opcion == "4":
            archivo = input("Ruta del CSV: ")
            cargar_csv(avl, archivo)

        elif opcion == "5":
            avl.graficar()

        elif opcion == "6":
            break

        else:
            print("Opción inválida")



# EJECUCIÓN

if __name__ == "__main__":
    menu()