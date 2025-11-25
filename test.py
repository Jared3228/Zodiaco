from motor import inferir_compatibilidad


def main():
    print("=== Sistema experto de compatibilidad zodiacal ===\n")

    signo1 = input("Primer signo: ")
    signo2 = input("Segundo signo: ")

    resultado = inferir_compatibilidad(signo1, signo2)

    # Si hubo error con algún signo
    if "error" in resultado:
        print("\n[ERROR]")
        print(resultado["error"])
        return

    print("\n--- Resultado ---")
    print(f"Signos: {resultado['signo1'].capitalize()} y {resultado['signo2'].capitalize()}")
    print(f"Elementos: {resultado['elemento1']} y {resultado['elemento2']}")
    print(f"Nivel base: {resultado['nivel'].capitalize()}")
    print(f"Compatibilidad aproximada: {resultado['porcentaje']}%")
    print(f"Descripción corta: {resultado['descripcion']}")
    print("\nMensaje detallado:")
    print(resultado["mensaje_detallado"])
    print("\n=============================\n")


if __name__ == "__main__":
    main()
