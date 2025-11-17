# altas_locales_dgip_

locales = []

# Pedir respuesta S/N
def preguntar(texto):
    return input(texto + " (s/n): ").strip().lower() == "s"

# Validar requisitos según tipo
def validar_requisitos(s):
    faltantes = []

    if not s["constancia_arca"]:
        faltantes.append("Constancia AFIP/ARCA")
    if not s["factura_luz"]:
        faltantes.append("Factura de luz o cédula parcelaria")
    if not s["contrato"]:
        faltantes.append("Contrato de locación/comodato")
    if not s["dni"]:
        faltantes.append("Fotocopia de DNI")
    if not s["cuit"]:
        faltantes.append("Constancia de CUIT")

    # Requisitos extra para empresas
    if s["tipo"] == "empresa":
        if not s["estatuto"]:
            faltantes.append("Estatuto de la empresa")
        if not s["poder"]:
            faltantes.append("Poder del representante")

    return faltantes

# Cargar solicitud
def cargar_solicitud():
    print("\n--- Nueva solicitud de alta ---")
    nombre = input("Nombre del local: ")
    contrib = input("Nombre del contribuyente: ")

    print("Tipo de contribuyente:")
    print("1) Persona física")
    print("2) Empresa")
    tipo = "persona_fisica" if input("Opción: ").strip() == "1" else "empresa"

    # Requisitos básicos
    s = {
        "nombre": nombre,
        "contribuyente": contrib,
        "tipo": tipo,
        "constancia_arca": preguntar("¿Presenta constancia AFIP/ARCA?"),
        "factura_luz": preguntar("¿Presenta factura de luz/cédula parcelaria?"),
        "contrato": preguntar("¿Presenta contrato de locación/comodato?"),
        "dni": preguntar("¿Presenta fotocopia de DNI?"),
        "cuit": preguntar("¿Presenta constancia de CUIT?"),
        "estatuto": False,
        "poder": False
    }

    # Requisitos para empresas
    if tipo == "empresa":
        s["estatuto"] = preguntar("¿Presenta estatuto de la empresa?")
        s["poder"] = preguntar("¿Presenta poder del representante?")

    faltantes = validar_requisitos(s)

    print("\n--- Resultado ---")
    if faltantes:
        print("La solicitud NO puede darse de alta. Faltan:")
        for f in faltantes:
            print(" -", f)
    else:
        locales.append(s)
        print("Solicitud aprobada. Alta registrada.")
        print("ID interno:", len(locales))
        print("\nDerivar a Habilitaciones con:")
        print(" - Formulario de seguridad industrial")
        print(" - Prefactibilidad")
        print(" - Pago de constancia de bomberos")

# Menú principal
def main():
    print("=== Sistema de Altas Comerciales ===")

    while True:
        print("\n1) Cargar solicitud")
        print("2) Ver cantidad de altas registradas")
        print("0) Salir")
        op = input("Opción: ")

        if op == "1":
            cargar_solicitud()
        elif op == "2":
            print("Locales dados de alta:", len(locales))
        elif op == "0":
            print("Saliendo.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()