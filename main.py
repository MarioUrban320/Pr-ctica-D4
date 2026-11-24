
from decimal import Decimal, InvalidOperation


# Lista donde se guardarán todas las ventas
ventas = []


def pedir_opcion():
    """Solicita una opción del menú y controla posibles errores."""
    try:
        return int(input("Selecciona una opción: "))
    except ValueError:
        print("Error: debes introducir un número entero.")
        return -1


def pedir_importe():
    """Solicita el importe de una venta y comprueba que sea válido."""
    while True:
        try:
            texto = input("Introduce el importe de la venta (€): ")
            importe = Decimal(texto.replace(",", "."))

            if not importe.is_finite() or importe <= 0:
                print("El importe debe ser un número mayor que cero.")
            else:
                return importe.quantize(Decimal("0.01"))

        except InvalidOperation:
            print("Error: introduce un importe válido.")


def pedir_forma_pago():
    """Solicita y valida la forma de pago."""
    while True:
        print("\nFormas de pago:")
        print("1. Efectivo")
        print("2. Tarjeta")
        print("3. Bizum")

        opcion = pedir_opcion()

        match opcion:
            case 1:
                return "Efectivo"
            case 2:
                return "Tarjeta"
            case 3:
                return "Bizum"
            case _:
                print("Opción incorrecta. Inténtalo de nuevo.")


def registrar_venta():
    """Registra una venta con su importe y forma de pago."""
    print("\n--- REGISTRAR VENTA ---")

    importe = pedir_importe()
    forma_pago = pedir_forma_pago()

    venta = {
        "importe": importe,
        "forma_pago": forma_pago
    }

    ventas.append(venta)

    print("Venta registrada correctamente.")
    print(f"Importe: {importe:.2f} €")
    print(f"Forma de pago: {forma_pago}")


def anular_ultima_venta():
    """Anula la última venta registrada."""
    print("\n--- ANULAR ÚLTIMA VENTA ---")

    if len(ventas) == 0:
        print("No hay ventas para anular.")
    else:
        venta = ventas.pop()

        print("Última venta anulada correctamente.")
        print(f"Importe anulado: {venta['importe']:.2f} €")


def calcular_total():
    """Calcula el importe total de todas las ventas."""
    total = Decimal("0.00")

    # Patrón de recorrido y acumulación
    for venta in ventas:
        total += venta["importe"]

    return total


def contar_operaciones():
    """Cuenta el número total de ventas registradas."""
    contador = 0

    # Patrón de recorrido y contador
    for venta in ventas:
        contador += 1

    return contador


def calcular_media():
    """Calcula el importe medio de las ventas."""
    cantidad = contar_operaciones()

    if cantidad == 0:
        return Decimal("0.00")

    total = calcular_total()
    return (total / cantidad).quantize(Decimal("0.01"))


def obtener_venta_mayor():
    """Devuelve la venta de mayor importe o None si no hay ventas."""
    if len(ventas) == 0:
        return None

    mayor = ventas[0]

    # Patrón de recorrido y máximo
    for venta in ventas:
        if venta["importe"] > mayor["importe"]:
            mayor = venta

    return mayor


def consultar_caja():
    """Muestra las estadísticas actuales de la caja."""
    print("\n--- RESUMEN DE CAJA ---")

    total = calcular_total()
    operaciones = contar_operaciones()
    media = calcular_media()
    mayor = obtener_venta_mayor()

    print(f"Total del día: {total:.2f} €")
    print(f"Número de operaciones: {operaciones}")
    print(f"Importe medio: {media:.2f} €")

    if mayor is None:
        print("Venta mayor: No hay ventas registradas.")
    else:
        print(f"Venta mayor: {mayor['importe']:.2f} €")
        print(f"Forma de pago: {mayor['forma_pago']}")


def cerrar_caja():
    """Muestra el resumen final de la caja."""
    print("\n========== CIERRE DE CAJA ==========")

    consultar_caja()

    print("\nCaja cerrada correctamente.")
    print("Gracias por utilizar el programa.")


def mostrar_menu():
    """Muestra las opciones disponibles del programa."""
    print("\n========== GESTOR DE CAJA ==========")
    print("1. Registrar una venta")
    print("2. Anular la última venta")
    print("3. Consultar resumen de caja")
    print("4. Cerrar caja")
    print("====================================")


def main():
    """Ejecuta el menú principal del gestor de caja."""
    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        match opcion:
            case 1:
                registrar_venta()

            case 2:
                anular_ultima_venta()

            case 3:
                consultar_caja()

            case 4:
                cerrar_caja()
                break

            case _:
                print("Opción incorrecta. Selecciona del 1 al 4.")


# Inicio del programa
if __name__ == "__main__":
    main()
