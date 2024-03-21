# Ejercicio 1: ¿Es un Número Primo?
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = int(input("Ingrese un número entero: "))
    if es_primo(num):
        print(num, "es un número primo.")
    else:
        print(num, "no es un número primo.")

# Ejercicio 2: Primo Siguiente
def siguiente_primo(n):
    n += 1
    while True:
        if es_primo(n):
            return n
        n += 1

if __name__ == "__main__":
    num = int(input("Ingrese un número entero: "))
    print("El siguiente número primo después de", num, "es:", siguiente_primo(num))

# Ejercicio 3: Mediana de Tres Valores
def mediana_de_tres(num1, num2, num3):
    nums = [num1, num2, num3]
    nums.sort()
    return nums[1]

if __name__ == "__main__":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    print("La mediana es:", mediana_de_tres(num1, num2, num3))

# Ejercicio 4: Contraseña Aleatoria
import random

def generar_contraseña_aleatoria():
    longitud = random.randint(7, 10)
    contraseña = ""
    for _ in range(longitud):
        contraseña += chr(random.randint(33, 126))
    return contraseña

if __name__ == "__main__":
    print("Contraseña generada aleatoriamente:", generar_contraseña_aleatoria())

# Ejercicio 5: Calcular la Hipotenusa
def calcular_hipotenusa(lado1, lado2):
    hipotenusa = (lado1**2 + lado2**2)**0.5
    return hipotenusa

if __name__ == "__main__":
    lado1 = float(input("Ingrese la longitud del primer lado más corto: "))
    lado2 = float(input("Ingrese la longitud del segundo lado más corto: "))
    print("La longitud de la hipotenusa es:", calcular_hipotenusa(lado1, lado2))
