# Función para calcular el interés simple
def calcular_interes_simple(principal, tasa, tiempo):
    """
    Calcula el interés simple dado el principal, la tasa y el tiempo.
    
    Parámetros:
    principal (float): El monto principal.
    tasa (float): La tasa de interés anual (en decimal, ej. 0.11 para 11%).
    tiempo (float): El tiempo en años.
    
    Retorna:
    float: El interés simple calculado.
    """
    interes = principal * tasa * tiempo
    return interes

# Ejemplo de uso con los valores dados
tasa = 0.11  # 11% efectiva anual
tiempo = 3    # 3 años

# Pedir al usuario el principal
principal = float(input("Ingrese el monto principal: "))

# Calcular el interés
interes = calcular_interes_simple(principal, tasa, tiempo)

# Mostrar el resultado
print(f"El interés simple para un principal de {principal} a una tasa del 11% durante 3 años es: {interes:.2f}")

# También mostrar el monto total
total = principal + interes
print(f"El monto total sería: {total:.2f}")
