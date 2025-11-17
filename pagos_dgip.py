# sistema_pagos_dgip.py
# Versión más simple posible conservando todas las funciones reales

from datetime import datetime, date

# Caja diaria simple
caja = {
    "fecha": date.today(),
    "pagos": [],
    "cerrada": False
}

# Registrar un pago
def registrar_pago():
    if caja["cerrada"]:
        print("La caja está cerrada.")
        return

    print("\n--- Registrar pago ---")
    contrib = input("Contribuyente: ")

    print("1) Inmobiliario  2) Automotor  3) Actividades varias  4) Otro")
    tipo = input("Tipo de impuesto: ").strip()
    tipos = {"1": "inmobiliario", "2": "automotor", "3": "actividades_varias", "4": "otro"}
    tipo = tipos.get(tipo, "otro")

    print("1) Efectivo 2) Transferencia 3) QR 4) Tarj. Crédito 5) Tarj. Débito 6) Cheque 7) Macro 8) Link")
    medio = input("Medio de pago: ").strip()
    medios = {
        "1": "efectivo", "2": "transferencia", "3": "qr", "4": "tarjeta_credito",
        "5": "tarjeta_debito", "6": "cheque_electronico", "7": "boton_macro", "8": "link_pago"
    }
    medio = medios.get(medio, "efectivo")

    monto = float(input("Monto: ").replace(",", "."))
    empresa = input("¿Es pago de empresa? (s/n): ").lower() == "s"
    codigo = input("Código de operación (opcional): ") or "-"

    pago = {
        "contribuyente": contrib,
        "tipo": tipo,
        "medio": medio,
        "monto": monto,
        "fecha": datetime.now(),
        "empresa": empresa,
        "codigo": codigo
    }

    caja["pagos"].append(pago)
    print("Pago registrado.\n")

# Resumen parcial
def resumen():
    print("\n--- Resumen parcial ---")

    imp = {}
    mp = {}

    for p in caja["pagos"]:
        imp[p["tipo"]] = imp.get(p["tipo"], 0) + p["monto"]
        mp[p["medio"]] = mp.get(p["medio"], 0) + p["monto"]

    print("\nPor impuesto:")
    for k, v in imp.items():
        print(f"- {k}: {v:.2f}")

    print("\nPor medio de pago:")
    for k, v in mp.items():
        print(f"- {k}: {v:.2f}")

# Cerrar caja
def cerrar_caja():
    if caja["cerrada"]:
        print("La caja ya está cerrada.")
        return

    print("\n--- Cierre de caja ---")
    caja["cerrada"] = True

    totales_fisicos = {}

    # Todas las claves de medios
    medios = {
        "efectivo", "transferencia", "qr", "tarjeta_credito",
        "tarjeta_debito", "cheque_electronico", "boton_macro", "link_pago"
    }

    for m in medios:
        totales_fisicos[m] = float(input(f"Total físico para {m}: ").replace(",", "."))

    # Calcular totales registrados
    tot_reg = {m: 0 for m in medios}
    for p in caja["pagos"]:
        tot_reg[p["medio"]] += p["monto"]

    print("\n=== RESULTADO DEL CIERRE ===")
    for m in medios:
        dif = totales_fisicos[m] - tot_reg[m]
        print(f"{m}: registrado={tot_reg[m]:.2f}, físico={totales_fisicos[m]:.2f}, diferencia={dif:.2f}")

# Pagos de empresas
def ver_empresas():
    print("\n--- Pagos de empresas ---")
    empresas = [p for p in caja["pagos"] if p["empresa"]]

    if not empresas:
        print("No hay pagos de empresas.")
        return

    for p in empresas:
        print(f"- {p['contribuyente']} | {p['tipo']} | {p['medio']} | {p['monto']:.2f} | {p['codigo']}")

# Menú principal
def main():
    print("=== Sistema DGIP ===")
    print("Fecha:", caja["fecha"])

    while True:
        print("\n1) Registrar pago")
        print("2) Ver resumen")
        print("3) Cerrar caja")
        print("4) Pagos de empresas")
        print("0) Salir")

        op = input("Opción: ").strip()

        if op == "1": registrar_pago()
        elif op == "2": resumen()
        elif op == "3": cerrar_caja()
        elif op == "4": ver_empresas()
        elif op == "0": break
        else:
            print("Opción inválida.")

if __name__ == "__main__":

    main()
