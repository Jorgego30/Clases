'''Generaliza el programa 2 de esta actividad:
Tienes dos jarras, una de X litros y otra de Y litros, con X>Y. Ninguna de las jarras tiene marcas en ella.
Hay una bomba que se puede utilizar para llenar las jarras con agua. ¿Cómo se pueden obtener
exactamente X/2 litros de agua en la jarra de X litros?'''

def obtener_X_medio(X, Y):
    # Llenar jarra Y
    agua_en_Y = Y

    # Verter agua de Y a X
    agua_en_X = agua_en_Y

    # Llenar jarra Y nuevamente
    agua_en_Y = Y

    # Verter agua de Y a X hasta obtener X/2 litros en X
    while agua_en_X < X / 2:
        agua_a_trasvasar = min(agua_en_Y, X / 2 - agua_en_X)
        agua_en_X += agua_a_trasvasar
        agua_en_Y -= agua_a_trasvasar

    return agua_en_X

# Definir capacidades de las jarras
X = 8  # Capacidad de la jarra X
Y = 5  # Capacidad de la jarra Y

# Obtener X/2 litros en la jarra de X litros
agua_X_medio = obtener_X_medio(X, Y)
print(f"Se obtuvieron exactamente {agua_X_medio} litros en la jarra de X litros.")