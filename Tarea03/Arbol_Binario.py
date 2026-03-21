"""
Sistema de Gestión de Árbol Binario de Búsqueda (ABB)
Permite crear, manipular y visualizar un ABB con interfaz CLI y generación de gráficos Graphviz
"""

import os
import subprocess
import sys
from typing import Optional, List, Union

class NodoABB:
    """Clase que representa un nodo del Árbol Binario de Búsqueda"""
    
    def __init__(self, valor: int):
        self.valor = valor
        self.izquierdo: Optional['NodoABB'] = None
        self.derecho: Optional['NodoABB'] = None
        self.altura = 1

class ArbolBinarioBusqueda:
    """Clase principal que implementa el Árbol Binario de Búsqueda"""
    
    def __init__(self):
        self.raiz: Optional[NodoABB] = None
        self.dot_counter = 0
    
    def insertar(self, valor: int) -> None:
        if self.raiz is None:
            self.raiz = NodoABB(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo: NodoABB, valor: int) -> NodoABB:
        if nodo is None:
            return NodoABB(valor)
        
        if valor < nodo.valor:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, valor)
        else:
            print(f"El valor {valor} ya existe en el árbol")
            return nodo
        
        nodo.altura = 1 + max(
            self._obtener_altura(nodo.izquierdo),
            self._obtener_altura(nodo.derecho)
        )
        
        return nodo
    
    def _obtener_altura(self, nodo: Optional[NodoABB]) -> int:
        return nodo.altura if nodo else 0
    
    def buscar(self, valor: int) -> bool:
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, nodo: Optional[NodoABB], valor: int) -> bool:
        if nodo is None:
            return False
        
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo.derecho, valor)
    
    def eliminar(self, valor: int) -> bool:
        if not self.buscar(valor):
            return False
        
        self.raiz = self._eliminar_recursivo(self.raiz, valor)
        return True
    
    def _eliminar_recursivo(self, nodo: Optional[NodoABB], valor: int) -> Optional[NodoABB]:
        if nodo is None:
            return None
        
        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, valor)
        else:
            if nodo.izquierdo is None and nodo.derecho is None:
                return None
            
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo
            
            sucesor = self._encontrar_minimo(nodo.derecho)
            nodo.valor = sucesor.valor
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, sucesor.valor)
        
        return nodo
    
    def _encontrar_minimo(self, nodo: NodoABB) -> NodoABB:
        actual = nodo
        while actual.izquierdo:
            actual = actual.izquierdo
        return actual
    
    def cargar_desde_archivo(self, ruta_archivo: str) -> int:
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"El archivo {ruta_archivo} no existe")
        
        elementos_insertados = 0
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                
                if ',' in contenido:
                    numeros = contenido.replace('\n', ',').split(',')
                elif ';' in contenido:
                    numeros = contenido.replace('\n', ';').split(';')
                else:
                    numeros = contenido.split()
                
                for num_str in numeros:
                    num_str = num_str.strip()
                    if num_str and num_str.replace('-', '').isdigit():
                        try:
                            valor = int(num_str)
                            self.insertar(valor)
                            elementos_insertados += 1
                        except ValueError:
                            print(f"Valor no válido ignorado: {num_str}")
        except Exception as e:
            raise Exception(f"Error al leer el archivo: {str(e)}")
        
        return elementos_insertados
    
    def generar_grafico(self, nombre_archivo: str = "arbol") -> bool:
        if self.raiz is None:
            print("El árbol está vacío, no se puede generar gráfico")
            return False
        
        nombre_completo = f"{nombre_archivo}_{self.dot_counter}"
        dot_content = self._generar_dot()
        
        archivo_dot = f"{nombre_completo}.dot"
        with open(archivo_dot, 'w', encoding='utf-8') as f:
            f.write(dot_content)
        
        print(f"Archivo DOT generado: {archivo_dot}")
        
        try:
            subprocess.run(['dot', '-Tpng', archivo_dot, '-o', f"{nombre_completo}.png"], 
                         check=True, capture_output=True)
            print(f"Gráfico generado: {nombre_completo}.png")
            self.dot_counter += 1
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Graphviz no está instalado o no se pudo generar la imagen")
            print(f"Puedes visualizar el archivo {archivo_dot} con un visor de DOT")
            return False
    
    def _generar_dot(self) -> str:
        lines = ['digraph ArbolBinarioBusqueda {',
                '    node [shape=circle, style=filled, fillcolor=lightblue];',
                '    edge [color=gray];']
        
        if self.raiz:
            self._generar_nodos_dot(self.raiz, lines)
        
        lines.append('}')
        return '\n'.join(lines)
    
    def _generar_nodos_dot(self, nodo: NodoABB, lines: List[str]) -> None:
        if nodo.izquierdo:
            lines.append(f'    "{nodo.valor}" -> "{nodo.izquierdo.valor}" [label="<"];')
            self._generar_nodos_dot(nodo.izquierdo, lines)
        
        if nodo.derecho:
            lines.append(f'    "{nodo.valor}" -> "{nodo.derecho.valor}" [label=">"];')
            self._generar_nodos_dot(nodo.derecho, lines)

class InterfazABB:
    
    def __init__(self):
        self.arbol = ArbolBinarioBusqueda()
        self.ejecutando = True
    
    def mostrar_menu(self):
        print("\n" + "="*50)
        print("SISTEMA DE GESTIÓN DE ÁRBOL BINARIO DE BÚSQUEDA")
        print("="*50)
        print("1. Insertar número")
        print("2. Buscar número")
        print("3. Eliminar número")
        print("4. Cargar desde archivo")
        print("5. Convertir a binario (generar gráfico)")
        print("6. Visualizar árbol (en texto)")
        print("7. Salir")
        print("="*50)
    
    def ejecutar(self):
        while self.ejecutando:
            self.mostrar_menu()
            opcion = input("Selecciona una opción (1-7): ").strip()
            
            if opcion == '1':
                self.opcion_insertar()
            elif opcion == '2':
                self.opcion_buscar()
            elif opcion == '3':
                self.opcion_eliminar()
            elif opcion == '4':
                self.opcion_cargar_archivo()
            elif opcion == '5':
                self.opcion_generar_grafico()
            elif opcion == '6':
                self.opcion_visualizar_texto()
            elif opcion == '7':
                self.opcion_salir()
            else:
                print("Opción no válida. Por favor, selecciona una opción del 1 al 7.")
    
    def opcion_insertar(self):
        try:
            valor = int(input("Ingresa el número a insertar: ").strip())
            self.arbol.insertar(valor)
            print(f"Número {valor} insertado correctamente")
        except ValueError:
            print("Error: Debes ingresar un número entero válido")
    
    def opcion_buscar(self):
        try:
            valor = int(input("Ingresa el número a buscar: ").strip())
            if self.arbol.buscar(valor):
                print(f"El número {valor} SÍ existe en el árbol")
            else:
                print(f"El número {valor} NO existe en el árbol")
        except ValueError:
            print("Error: Debes ingresar un número entero válido")
    
    def opcion_eliminar(self):
        try:
            valor = int(input("Ingresa el número a eliminar: ").strip())
            if self.arbol.eliminar(valor):
                print(f"Número {valor} eliminado correctamente")
            else:
                print(f"El número {valor} no existe en el árbol")
        except ValueError:
            print("Error: Debes ingresar un número entero válido")
    
    def opcion_cargar_archivo(self):
        print("\nCARGAR DESDE ARCHIVO")
        print("Ejemplos de archivos:")
        print("  - numeros.csv")
        print("  - datos.txt")
        print("  - enteros.csv")
        
        ruta = input("Ingresa la ruta del archivo: ").strip()
        
        try:
            cantidad = self.arbol.cargar_desde_archivo(ruta)
            print(f"Se cargaron {cantidad} números correctamente")
            self.arbol.generar_grafico("arbol_cargado")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{ruta}'")
        except Exception as e:
            print(f"Error al cargar el archivo: {str(e)}")
    
    def opcion_generar_grafico(self):
        nombre = input("Ingresa el nombre base para el archivo (Enter para 'arbol'): ").strip()
        if not nombre:
            nombre = "arbol"
        
        self.arbol.generar_grafico(nombre)
    
    def opcion_visualizar_texto(self):
        if self.arbol.raiz is None:
            print("El árbol está vacío")
        else:
            print("\nREPRESENTACIÓN DEL ÁRBOL (in-order):")
            self._mostrar_en_orden(self.arbol.raiz)
            print()
    
    def _mostrar_en_orden(self, nodo: Optional[NodoABB], nivel: int = 0):
        if nodo:
            self._mostrar_en_orden(nodo.derecho, nivel + 1)
            print("    " * nivel + f"└── {nodo.valor}")
            self._mostrar_en_orden(nodo.izquierdo, nivel + 1)
    
    def opcion_salir(self):
        print("\nGracias por usar el sistema de Árbol Binario de Búsqueda")
        self.ejecutando = False

def crear_archivos_ejemplo():
    ejemplos = {
        "numeros_ejemplo1.csv": "50,30,70,20,40,60,80",
        "numeros_ejemplo2.txt": "15 10 20 8 12 17 25",
        "enteros_ejemplo3.csv": "100;50;150;25;75;125;175"
    }
    
    for nombre, contenido in ejemplos.items():
        with open(nombre, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print(f"Archivo de ejemplo creado: {nombre}")

def main():
    print("Iniciando Sistema de Árbol Binario de Búsqueda...")
    
    try:
        crear_archivos_ejemplo()
    except Exception as e:
        print(f"No se pudieron crear los archivos de ejemplo: {e}")
    
    interfaz = InterfazABB()
    interfaz.ejecutar()

if __name__ == "__main__":
    main()