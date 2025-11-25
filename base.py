# Signos del zodiaco y sus elementos
hechos_signos = {
    "aries": ["fuego"],
    "leo": ["fuego"],
    "sagitario": ["fuego"],
    "cancer": ["agua"],
    "escorpio": ["agua"],
    "piscis": ["agua"],
    "tauro": ["tierra"],
    "virgo": ["tierra"],
    "capricornio": ["tierra"],
    "geminis": ["aire"],
    "libra": ["aire"],
    "acuario": ["aire"]
}

# Reglas de compatibilidad
reglas_compatibilidad = [
    ("fuego", "aire", "alta"),
    ("aire", "fuego", "alta"),
    ("agua", "tierra", "alta"),
    ("tierra", "agua", "alta"),
    ("fuego", "agua", "baja"),
    ("aire", "tierra", "baja"),
]
