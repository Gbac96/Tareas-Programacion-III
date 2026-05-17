import csv
import os
from btree import BTree


def menu():
    print("\n--- SISTEMA DE ÁRBOL B ---")
    print("1. Configurar grado del Árbol (T)")
    print("2. Insertar clave")
    print("3. Buscar clave")
    print("4. Eliminar clave")
    print("5. Cargar datos desde CSV")
    print("6. Generar representación gráfica (Graphviz)")
    print("7. Salir")
    return input("Seleccione una opción: ")


def main():
    arbol = None

    while True:
        opcion = menu()

        if opcion == '1':
            grado = int(input("Ingrese el grado mínimo (T) del Árbol B (ej. 3): "))
            arbol = BTree(grado)
            print(f"Árbol B inicializado con grado {grado}.")

        elif opcion == '2':
            if not arbol: print("Debe inicializar el árbol primero (Opción 1)."); continue
            clave = int(input("Ingrese la clave a insertar (número entero): "))
            arbol.insert(clave)
            print(f"Clave {clave} insertada.")

        elif opcion == '3':
            if not arbol: print("Debe inicializar el árbol primero."); continue
            clave = int(input("Ingrese la clave a buscar: "))
            encontrado = arbol.search(clave)
            if encontrado:
                print(f"¡Clave {clave} encontrada en el árbol!")
            else:
                print(f"Clave {clave} NO existe en el árbol.")

        elif opcion == '4':
            if not arbol: print("Debe inicializar el árbol primero."); continue
            clave = int(input("Ingrese la clave a eliminar: "))
            arbol.delete(arbol.root, clave)
            print(f"Operación de eliminación ejecutada para la clave {clave}.")

        elif opcion == '5':
            if not arbol: print("Debe inicializar el árbol primero."); continue
            archivo = input("Ingrese el nombre del archivo CSV (ej. datos1.csv): ")
            if os.path.exists(archivo):
                with open(archivo, mode='r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    next(reader)  # Saltar cabecera
                    contador = 0
                    for row in reader:
                        try:
                            # Asumimos que la primera columna del CSV es un ID entero
                            clave = int(row[0])
                            arbol.insert(clave)
                            contador += 1
                        except ValueError:
                            pass
                print(f"Carga masiva completada: {contador} registros insertados.")
            else:
                print("Archivo no encontrado. Verifique el nombre y la ruta.")

        elif opcion == '6':
            if not arbol: print("Debe inicializar el árbol primero."); continue
            nombre_salida = input("Ingrese el nombre del archivo de salida para la gráfica (sin extensión): ")
            arbol.draw_graph(nombre_salida)

        elif opcion == '7':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()