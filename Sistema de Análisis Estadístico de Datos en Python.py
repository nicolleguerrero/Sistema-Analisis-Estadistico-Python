
import statistics
import csv
import math
from collections import Counter


class AnalizadorDatos:
    def __init__(self):
        self.datos = []

    def ingresar_datos(self):
        print("\nINGRESAR DATOS")
        entrada = input("Introduce numeros separados por comas: ")

        try:
            nuevos = [
                float(numero.strip())
                for numero in entrada.split(",")
            ]

            if not nuevos or not all(math.isfinite(n) for n in nuevos):
                raise ValueError

            self.datos = nuevos
            print("Datos guardados correctamente.")

        except ValueError:
            print("Error: introduce solamente numeros validos.")

    def mostrar_datos(self):
        if not self.datos:
            print("\nNo hay datos registrados.")
            return

        print("\nDATOS REGISTRADOS")
        for i, valor in enumerate(self.datos, start=1):
            print(f"{i}. {valor:g}")

    def calcular_estadisticas(self):
        if not self.datos:
            print("\nPrimero debes ingresar datos.")
            return

        datos = self.datos

        print("\nESTADISTICAS DESCRIPTIVAS")
        print("-" * 35)
        print(f"Cantidad: {len(datos)}")
        print(f"Suma: {sum(datos):.2f}")
        print(f"Media: {statistics.mean(datos):.2f}")
        print(f"Mediana: {statistics.median(datos):.2f}")

        modas = statistics.multimode(datos)
        frecuencias = Counter(datos)

        if max(frecuencias.values()) == 1:
            print("Moda: No existe")
        else:
            print("Moda:", ", ".join(f"{n:g}" for n in modas))

        print(f"Minimo: {min(datos):.2f}")
        print(f"Maximo: {max(datos):.2f}")
        print(f"Rango: {max(datos) - min(datos):.2f}")

        if len(datos) > 1:
            print(f"Varianza: {statistics.variance(datos):.2f}")
            print(f"Desviacion estandar: {statistics.stdev(datos):.2f}")
        else:
            print("Varianza: Se necesitan al menos 2 datos")
            print("Desviacion estandar: Se necesitan al menos 2 datos")

    def grafico_barras(self):
        if not self.datos:
            print("\nPrimero debes ingresar datos.")
            return

        print("\nGRAFICO DE BARRAS")
        print("-" * 45)

        maximo = max(abs(n) for n in self.datos)

        for i, valor in enumerate(self.datos, start=1):
            longitud = round(abs(valor) / maximo * 35) if maximo else 0
            barra = "#" * longitud
            print(f"Dato {i:2} | {barra} {valor:g}")

        print("\nEscala proporcional al valor absoluto.")

    def histograma(self):
        if not self.datos:
            print("\nPrimero debes ingresar datos.")
            return

        print("\nHISTOGRAMA DE FRECUENCIAS")
        print("-" * 45)

        minimo = min(self.datos)
        maximo = max(self.datos)

        if minimo == maximo:
            print(f"{minimo:g} | {'#' * len(self.datos)} ({len(self.datos)})")
            return

        cantidad_intervalos = min(5, len(self.datos))
        ancho = (maximo - minimo) / cantidad_intervalos

        for i in range(cantidad_intervalos):
            inicio = minimo + i * ancho
            fin = inicio + ancho

            if i == cantidad_intervalos - 1:
                frecuencia = sum(
                    inicio <= n <= fin for n in self.datos
                )
            else:
                frecuencia = sum(
                    inicio <= n < fin for n in self.datos
                )

            barra = "#" * frecuencia
            print(
                f"{inicio:8.2f} - {fin:8.2f} | "
                f"{barra} ({frecuencia})"
            )

    def guardar_csv(self):
        if not self.datos:
            print("\nNo hay datos para guardar.")
            return

        nombre = "resultados_analisis.csv"

        try:
            with open(nombre, "w", newline="", encoding="utf-8") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(["Numero", "Valor"])

                for i, valor in enumerate(self.datos, start=1):
                    escritor.writerow([i, valor])

                escritor.writerow([])
                escritor.writerow(["Estadistica", "Resultado"])
                escritor.writerow(["Cantidad", len(self.datos)])
                escritor.writerow(["Media", statistics.mean(self.datos)])
                escritor.writerow(["Mediana", statistics.median(self.datos)])
                escritor.writerow(["Minimo", min(self.datos)])
                escritor.writerow(["Maximo", max(self.datos)])

                if len(self.datos) > 1:
                    escritor.writerow([
                        "Desviacion estandar muestral",
                        statistics.stdev(self.datos)
                    ])

            print(f"\nArchivo guardado: {nombre}")

        except OSError as error:
            print(f"No se pudo guardar el archivo: {error}")


def mostrar_menu():
    print("\n" + "=" * 48)
    print("       SISTEMA DE ANALISIS DE DATOS")
    print("=" * 48)
    print("1. Ingresar datos")
    print("2. Mostrar datos")
    print("3. Calcular estadisticas")
    print("4. Generar grafico de barras")
    print("5. Generar histograma")
    print("6. Exportar resultados a CSV")
    print("7. Salir")
    print("=" * 48)


def main():
    analizador = AnalizadorDatos()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion (1-7): ").strip()

        if opcion == "1":
            analizador.ingresar_datos()

        elif opcion == "2":
            analizador.mostrar_datos()

        elif opcion == "3":
            analizador.calcular_estadisticas()

        elif opcion == "4":
            analizador.grafico_barras()

        elif opcion == "5":
            analizador.histograma()

        elif opcion == "6":
            analizador.guardar_csv()

        elif opcion == "7":
            print("\nGracias por utilizar el analizador.")
            break

        else:
            print("\nOpcion no valida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
