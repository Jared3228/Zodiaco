# motor.py

"""
Motor de inferencia para el sistema de compatibilidad zodiacal.

Utiliza:
- Encadenamiento hacia adelante muy simple: a partir de los signos,
  obtiene los elementos y luego aplica reglas de compatibilidad.
- Una función recursiva para buscar la regla aplicable.
- Un sistema cosmetico
"""

import random
from base import hechos_signos, reglas_compatibilidad

# Descripción corta según el nivel
descripcion_por_nivel = lambda nivel: {
    "alta": "Alta compatibilidad: buena conexión y entendimiento.",
    "media": "Compatibilidad media: puede funcionar con comunicación.",
    "baja": "Baja compatibilidad: pueden existir muchos roces.",
}.get(nivel, "Compatibilidad no determinada.")


def normalizar_signo(signo: str) -> str:
    """Limpia la entrada del usuario."""
    return signo.strip().lower()


def buscar_regla_recursiva(elemento1: str, elemento2: str, indice: int = 0) -> str:
    """
    Busca de forma RECURSIVA una regla de compatibilidad que coincida
    con los elementos dados.

    elemento1: elemento del primer signo (fuego, agua, etc.)
    elemento2: elemento del segundo signo
    indice: índice actual en la lista de reglas
    return: nivel de compatibilidad ("alta", "media", "baja")
    """
    if indice >= len(reglas_compatibilidad):
        # Caso base: no se encontró ninguna regla específica → media por defecto
        return "media"

    actual = reglas_compatibilidad[indice]
    if actual[0] == elemento1 and actual[1] == elemento2:
        return actual[2]

    # Llamada recursiva avanzando al siguiente índice
    return buscar_regla_recursiva(elemento1, elemento2, indice + 1)



def rango_por_nivel(nivel: str) -> tuple[int, int]:
    """
    Asigna un rango de porcentaje según el nivel base.

    baja  →  0–33
    media → 34–66
    alta  → 67–100
    """
    if nivel == "baja":
        return (0, 33)
    if nivel == "media":
        return (34, 66)
    if nivel == "alta":
        return (67, 100)
    # fallback por si llega algo raro
    return (0, 100)


def mensaje_por_porcentaje(porcentaje: int, nivel: str) -> str:
    """
    Devuelve un mensaje largo según el rango del porcentaje.
    No tiene mucha logica.
    """
    if 0 <= porcentaje <= 9:
        return (
            f"Entre sus energías se percibe una compatibilidad casi experimental. "
            f"Es como si el universo estuviera apenas haciendo pruebas A/B con ustedes "
            f"({porcentaje}%). Nada está escrito, pero todo puede sorprender."
        )
    elif 10 <= porcentaje <= 19:
        return (
            f"Hay chispas aisladas que aparecen de vez en cuando ({porcentaje}%), "
            f"como conversaciones que se alargan de la nada y luego se apagan. "
            f"No es la dupla más obvia, pero eso también tiene su encanto raro."
        )
    elif 20 <= porcentaje <= 29:
        return (
            f"La compatibilidad se mueve en una zona tímida ({porcentaje}%), "
            f"donde las coincidencias existen pero necesitan ser empujadas. "
            f"Con paciencia, podría haber momentos memorables entre estos signos."
        )
    elif 30 <= porcentaje <= 39:
        return (
            f"Se encuentra en un punto curioso ({porcentaje}%) donde la conexión "
            f"no es inmediata, pero tampoco inexistente. Hay oportunidades si "
            f"ambas partes deciden tomarse en serio la dinámica."
        )
    elif 40 <= porcentaje <= 49:
        return (
            f"La relación entre estos signos camina por una cuerda floja estable "
            f"({porcentaje}%). No es la pareja de manual, pero con acuerdos claros "
            f"podría construirse algo funcional y hasta cómodo."
        )
    elif 50 <= porcentaje <= 59:
        return (
            f"Están en una zona de equilibrio extraño ({porcentaje}%), donde los "
            f"choques se compensan con momentos de apoyo genuino. No es perfecto, "
            f"pero puede ser real, honesto y suficientemente bueno."
        )
    elif 60 <= porcentaje <= 69:
        return (
            f"La compatibilidad fluye con relativa naturalidad ({porcentaje}%). "
            f"Ambos signos tienen puntos de fricción, pero también una base "
            f"interesante para entenderse sin demasiadas instrucciones."
        )
    elif 70 <= porcentaje <= 79:
        return (
            f"Hay una conexión notable ({porcentaje}%) que se nota en cómo se "
            f"acompañan y se retan. No todo será fácil, pero la química general "
            f"tiende a jugar más a favor que en contra."
        )
    elif 80 <= porcentaje <= 89:
        return (
            f"La compatibilidad se siente casi coreografiada ({porcentaje}%). "
            f"Las personalidades se complementan, se empujan a crecer y logran "
            f"un balance que pocas combinaciones alcanzan de forma natural."
        )
    elif 90 <= porcentaje <= 100:
        return (
            f"Esta combinación se sale de la estadística normal ({porcentaje}%). "
            f"Es el tipo de vínculo que puede volverse referencia para los demás: "
            f"intenso, intuitivo y con una sincronía que parece escrita a mano."
        )

    # fallback (por si acaso)
    return (
        f"La compatibilidad se mueve en un terreno difícil de etiquetar "
        f"({porcentaje}%). El nivel base es {nivel}, pero la historia real "
        f"la escriben los detalles del día a día."
    )


def generar_porcentaje_y_mensaje(nivel: str) -> tuple[int, str]:
    """
    A partir del nivel base, genera un porcentaje aleatorio dentro
    del rango correspondiente y un mensaje largo asociado.
    """
    minimo, maximo = rango_por_nivel(nivel)
    porcentaje = random.randint(minimo, maximo)
    mensaje = mensaje_por_porcentaje(porcentaje, nivel)
    return porcentaje, mensaje


# --- Función principal --- #

def inferir_compatibilidad(signo1: str, signo2: str) -> dict:
    """
    Dado el nombre de dos signos, infiere el nivel de compatibilidad
    usando la base de conocimiento y el motor de inferencia.

    return: diccionario con información de la compatibilidad:
        {
            "signo1": "...",
            "signo2": "...",
            "elemento1": "...",
            "elemento2": "...",
            "nivel": "alta/media/baja",
            "porcentaje": 0-100,
            "descripcion": "texto explicativo corto",
            "mensaje_detallado": "texto largo según porcentaje"
        }
    """
    signo1_norm = normalizar_signo(signo1)
    signo2_norm = normalizar_signo(signo2)

    elemento1 = hechos_signos.get(signo1_norm)
    elemento2 = hechos_signos.get(signo2_norm)

    errores = []
    if not elemento1:
        errores.append(f"Signo desconocido: {signo1}")
    if not elemento2:
        errores.append(f"Signo desconocido: {signo2}")

    if errores:
        # Regresamos un resultado estructurado con el error
        return {
            "signo1": signo1_norm,
            "signo2": signo2_norm,
            "error": " / ".join(errores)
        }

    # Por ahora solo usamos el primer elemento de la lista
    elemento1 = elemento1[0]
    elemento2 = elemento2[0]

    # Usamos la función RECURSIVA para encontrar el nivel
    nivel = buscar_regla_recursiva(elemento1, elemento2)

    # Generamos porcentaje + mensaje “de verbo”
    porcentaje, mensaje_detallado = generar_porcentaje_y_mensaje(nivel)

    descripcion = descripcion_por_nivel(nivel)

    return {
        "signo1": signo1_norm,
            "signo2": signo2_norm,
            "elemento1": elemento1,
            "elemento2": elemento2,
            "nivel": nivel,
            "porcentaje": porcentaje,
            "descripcion": descripcion,
            "mensaje_detallado": mensaje_detallado,
    }
