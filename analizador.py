# analizador.py
# Modulo encargado de la representacion y analisis de los resultados de clasificacion


class AnalizadorCalidad:
    def __init__(self, resultados):
        """
        resultados: Lista de diccionarios con la estructura:
        {
            'id': int,
            'huevo': objeto Huevo,
            'centroide': float,
            'clase': str
        }
        """
        self.resultados = resultados

    def ordenar_por_centroid(self, ascendente=False):
        """Ordena la lista de resultados segun el valor del centroide"""
        return sorted(
            self.resultados, key=lambda x: x["centroide"], reverse=not ascendente
        )

    def filtrar_por_clase(self, clase_objetivo):
        """Retorna solo los huevos que pertenecen a una clase especifica (A, B o C)."""
        return [
            r for r in self.resultados if clase_objetivo.upper() in r["clase"].upper()
        ]

    def obtener_por_id(self, id_buscado):
        """Busca y retorna el resultado de un huevo especifico por su ID."""
        for r in self.resultados:
            if r["id"] == id_buscado:
                return r
        return None

    # Necesita modificacion para que imprima la membresia de cada clase
    def imprimir_reporte_completo(self):
        """Imprime una tabla detallada con todos los resultados incluyendo membresias."""
        header = f"{'ID':<4} | {'Centroide':<10}  | {'μA':<6} | {'μB':<6} | {'μC':<6} | {'Clase':<25}"
        print(f"\n{header}")
        print("-" * len(header))
        cantA = 0
        cantB = 0
        cantC = 0
        for r in self.resultados:
            mA, mB, mC = r["membresias"]
            if mA > 0:
                cantA = cantA + 1
            if mB > 0:
                cantB = cantC + 1
            if mB > 0:
                cantC = cantC + 1
            print(
                f"{r['id']:03d}  | {r['centroide']:<10.2f}  | {mA:<6.2f} | {mB:<6.2f} | {mC:<6.2f} | {r['clase']:<25}"
            )

    def imprimir_estadisticas(self):
        """Muestra un resumen estadistico de la ejecucion."""
        total = len(self.resultados)
        if total == 0:
            return

        conteo = {}
        for r in self.resultados:
            # Extraemos el nombre de la clase (Clase A, B, etc)
            nombre_clase = (
                r["clase"].split(" - ")[0] if " - " in r["clase"] else r["clase"]
            )
            conteo[nombre_clase] = conteo.get(nombre_clase, 0) + 1

        print("\n" + "=" * 40)
        print("       RESUMEN DE CLASIFICACION")
        print("=" * 40)
        for clase, cantidad in sorted(conteo.items()):
            porcentaje = (cantidad / total) * 100
            print(f"{clase:<10}: {cantidad:>3} huevos ({porcentaje:>5.1f}%)")
        print("-" * 40)
        print(f"TOTAL     : {total:>3} huevos analizados")
        print("=" * 40)
