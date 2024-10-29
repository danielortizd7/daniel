def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Ejemplo de uso
peso = float(input("Introduce tu peso en kg: "))  # Pide al usuario el peso
altura = float(input("Introduce tu altura en metros: "))  # Pide al usuario la altura

imc = calcular_imc(peso, altura)
print("Tu IMC es:", round(imc, 2))
