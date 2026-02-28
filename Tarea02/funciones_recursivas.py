def convertir_a_binario(n):
    """
    Función recursiva que convierte un número entero a binario
    """
    if n < 0:
        return "-" + convertir_a_binario(abs(n))
    elif n < 2:
        return str(n)
    else:
        return convertir_a_binario(n // 2) + str(n % 2)

def contar_digitos(n):
    """
    Función recursiva que cuenta la cantidad de dígitos en un número entero
    """
    # Manejar números negativos
    n = abs(n)
    
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)

def raiz_cuadrada_entera(n):
    """
    Función principal que encuentra la raíz cuadrada entera de un número
    """
    if n < 0:
        return "No se puede calcular raíz cuadrada de un número negativo"
    
    def calcular_raiz_cuadrada(n, inicio, fin):
        """
        Función auxiliar recursiva para encontrar la raíz cuadrada entera
        """
        if inicio > fin:
            return fin
        
        medio = (inicio + fin) // 2
        cuadrado = medio * medio
        
        if cuadrado == n:
            return medio
        elif cuadrado < n:
            return calcular_raiz_cuadrada(n, medio + 1, fin)
        else:
            return calcular_raiz_cuadrada(n, inicio, medio - 1)
    
    return calcular_raiz_cuadrada(n, 0, n)

def convertir_a_decimal(romano):
    """
    Función que convierte un número romano a decimal usando recursividad
    """
    # Diccionario con valores de números romanos
    valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    if not romano:
        return 0
    
    if len(romano) == 1:
        return valores[romano[0]]
    
    # Verificar si es un caso de resta (ej: IV, IX, XL, etc.)
    if valores[romano[0]] < valores[romano[1]]:
        return (valores[romano[1]] - valores[romano[0]]) + convertir_a_decimal(romano[2:])
    else:
        return valores[romano[0]] + convertir_a_decimal(romano[1:])

def suma_numeros_enteros(n):
    """
    Función recursiva que suma todos los números desde 0 hasta n
    """
    if n < 0:
        return "No se puede sumar hasta un número negativo"
    
    if n == 0:
        return 0
    else:
        return n + suma_numeros_enteros(n - 1)

def validar_entero_positivo(mensaje, permitir_cero=True):
    """
    Valida que la entrada sea un número entero positivo
    """
    while True:
        try:
            numero = int(input(mensaje))
            if permitir_cero and numero >= 0:
                return numero
            elif not permitir_cero and numero > 0:
                return numero
            else:
                print("Por favor, ingrese un número válido.")
        except ValueError:
            print("Error: Debe ingresar un número entero.")

def validar_entero(mensaje):
    """
    Valida que la entrada sea un número entero (puede ser negativo)
    """
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número entero.")

def validar_romano(mensaje):
    """
    Valida que la entrada sea un número romano válido
    """
    while True:
        romano = input(mensaje).upper()
        if all(c in 'IVXLCDM' for c in romano) and romano:
            return romano
        else:
            print("Error: Debe ingresar un número romano válido (solo letras I, V, X, L, C, D, M).")

def mostrar_menu():
    """
    Muestra el menú principal del programa
    """
    print("\n" + "="*50)
    print("           FUNCIONES RECURSIVAS - MENÚ PRINCIPAL")
    print("="*50)
    print("1. Convertir a Binario")
    print("2. Contar Dígitos")
    print("3. Raíz Cuadrada Entera")
    print("4. Convertir a Decimal desde Romano")
    print("5. Suma de Números Enteros ")
    print("6. Salir")
    print("="*50)

def ejecutar_opcion(opcion):
    """
    Ejecuta la opción seleccionada por el usuario
    """
    if opcion == 1:
        print("\n--- CONVERTIR A BINARIO ---")
        numero = validar_entero("Ingrese un número entero: ")
        resultado = convertir_a_binario(numero)
        print(f"El número {numero} en binario es: {resultado}")
        
    elif opcion == 2:
        print("\n--- CONTAR DÍGITOS ---")
        numero = validar_entero("Ingrese un número entero: ")
        resultado = contar_digitos(numero)
        print(f"El número {numero} tiene {resultado} dígito(s)")
        
    elif opcion == 3:
        print("\n--- RAÍZ CUADRADA ENTERA ---")
        numero = validar_entero_positivo("Ingrese un número entero positivo: ")
        resultado = raiz_cuadrada_entera(numero)
        print(f"La raíz cuadrada entera de {numero} es: {resultado}")
        
    elif opcion == 4:
        print("\n--- CONVERTIR ROMANO A DECIMAL ---")
        romano = validar_romano("Ingrese un número romano: ")
        resultado = convertir_a_decimal(romano)
        print(f"El número romano {romano} en decimal es: {resultado}")
        
    elif opcion == 5:
        print("\n--- SUMA DE NÚMEROS ENTEROS ---")
        numero = validar_entero_positivo("Ingrese un número entero positivo: ")
        resultado = suma_numeros_enteros(numero)
        print(f"La suma de 0 hasta {numero} es: {resultado}")
        
    elif opcion == 6:
        print("\n¡Gracias por usar el programa! Hasta luego.")
        return False
    
    return True

def main():
    """
    Función principal del programa
    """
    print("\nBIENVENIDO AL PROGRAMA DE FUNCIONES RECURSIVAS")
    
    continuar = True
    while continuar:
        mostrar_menu()
        try:
            opcion = int(input("\nSeleccione una opción (1-6): "))
            if 1 <= opcion <= 6:
                continuar = ejecutar_opcion(opcion)
                if continuar:
                    input("\nPresione Enter para continuar...")
            else:
                print("Error: Opción no válida. Por favor, seleccione 1-6.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

if __name__ == "__main__":
   
    # Iniciar el modo interactivo
    main()




