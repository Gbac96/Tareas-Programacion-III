# Tarea01 Pyton 

## Integrantes

Nombre: Gerson Emanuel Bac Muyus.
Carnet: 9490-17-22584
Participación: 100%

## Cómo ejecutar.

1. Instalar dependencias:
   pip install graphviz

2. Ejecutar:
   python lista_doble.py
3. ## Requisitos Previos

1. **Python 3.x** instalado en el sistema.
2. Biblioteca **Graphviz** para Python:
   ```bash
   pip install graphviz

Cada modificación genera automáticamente una imagen llamada:
lista_doble.png

## Requisitos.

- Python 3.x
- Graphviz instalado en el sistema

# Tarea 01
## Funciones implementadas
- Convertir número entero a binario
- Contar dígitos de un número
- Calcular raíz cuadrada entera
- Convertir número romano a decimal
- Sumar enteros desde 0 hasta n

## Tarea 02

# Funciones Recursivas

Programa en Python que implementa diversas funciones recursivas y una interfaz CLI interactiva.

## Tarea04 
Implementar un programa interactivo en Python que permita a los usuarios crear, manipular y visualizar un Árbol AVL, extendiendo la funcionalidad de un Árbol Binario de Búsqueda (ABB). El programa debe proporcionar las siguientes funcionalidades:

Insertar elementos en el árbol, manteniendo el balance mediante las rotaciones necesarias.

Buscar elementos en el árbol.

Eliminar elementos, asegurando el reequilibrio del árbol.

Cargar datos desde un archivo CSV para construir el árbol.

Generar una representación en Graphviz del árbol resultante.

## Tarea06

Desarrollar un programa en Python que implemente un Árbol B configurable por el grado del nodo, permitiendo las siguientes funcionalidades:

Configuración inicial: Permitir ingresar el grado del Árbol B.

Operaciones básicas:
Insertar claves.
Buscar claves.
Eliminar claves.
Carga de datos desde archivos CSV.

##Instrucciones

Sigue las instrucciones del menú interactivo. **Debes iniciar seleccionando la opción 1** para definir el grado del Árbol B antes de hacer cualquier otra operación.

## Instrucciones para Cargar Archivos CSV

En la raíz del proyecto se incluyen tres archivos para pruebas masivas: `datos1.csv`, `datos2.csv` y `datos3.csv`.

1. En el menú principal, selecciona la **Opción 5**.
2. Cuando el sistema lo solicite, escribe el nombre del archivo exacto, incluyendo la extensión, por ejemplo: `datos1.csv`.
3. El programa leerá la primera columna de cada fila (asumiendo que es un ID numérico) y la insertará automáticamente en la estructura del Árbol B.
4. Una vez terminada la carga, puedes usar la **Opción 6** para generar la gráfica y comprobar la estabilidad del árbol después de la inserción masiva.

## Representación Gráfica
La opción 6 del menú genera un archivo `.dot` y automáticamente lo renderiza en un archivo `.png` en la misma carpeta del proyecto. El árbol está coloreado y estructurado en forma de registros para identificar fácilmente los nodos y sus divisiones.


## Requisitos
- Python 3.x (no requiere librerías externas)

## Cómo ejecutar
1. Clona el repositorio o descarga el archivo que quieras usar.
2. Abre una terminal en la carpeta donde se encuentra el archivo.
3. Ejecuta:
   ```bash
   python funciones_recursivas.py
