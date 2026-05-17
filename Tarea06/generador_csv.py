import csv
import random


def generar_csv(nombre_archivo, cantidad_registros):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Dato_Mock"])

        # Generar IDs únicos aleatorios
        ids = random.sample(range(1, 10000), cantidad_registros)
        for num_id in ids:
            writer.writerow([num_id, f"Registro_Prueba_{num_id}"])

    print(f"Archivo {nombre_archivo} creado con {cantidad_registros} registros.")


# Crear los 3 archivos solicitados
generar_csv("datos1.csv", 150)
generar_csv("datos2.csv", 200)
generar_csv("datos3.csv", 120)