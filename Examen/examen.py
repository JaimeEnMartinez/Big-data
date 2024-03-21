# Función para determinar si un número es primo
def es_primo(n):
    return False if n <= 1 else all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

# Función para encontrar el siguiente número primo
def siguiente_primo(n):
    n += 1
    while True:
        if es_primo(n):
            return n
        n += 1

# Función para calcular la mediana de tres números
def mediana_de_tres(num1, num2, num3):
    nums = [num1, num2, num3]
    nums.sort()
    return nums[1]

# Función para generar una contraseña aleatoria
import random

def generar_contraseña_aleatoria():
    longitud = random.randint(7, 10)
    contraseña = "".join(chr(random.randint(33, 126)) for _ in range(longitud))
    return contraseña

# Función para calcular la hipotenusa de un triángulo rectángulo
def calcular_hipotenusa(lado1, lado2):
    hipotenusa = (lado1**2 + lado2**2)**0.5
    return hipotenusa

# Función principal para solicitar al usuario qué función desea ejecutar y solicitar los valores necesarios
def main():
    opcion = input("Seleccione la función a ejecutar:\n1. Determinar si un número es primo\n2. Encontrar el siguiente número primo\n3. Calcular la mediana de tres números\n4. Generar una contraseña aleatoria\n5. Calcular la hipotenusa de un triángulo rectángulo\nIngrese el número de la opción deseada: ")

    if opcion == '1':
        num = int(input("Ingrese un número entero: "))
        print(num, "es un número primo." if es_primo(num) else "no es un número primo.")
    elif opcion == '2':
        num = int(input("Ingrese un número entero: "))
        print("El siguiente número primo después de", num, "es:", siguiente_primo(num))
    elif opcion == '3':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        num3 = float(input("Ingrese el tercer número: "))
        print("La mediana es:", mediana_de_tres(num1, num2, num3))
    elif opcion == '4':
        print("Contraseña generada aleatoriamente:", generar_contraseña_aleatoria())
    elif opcion == '5':
        lado1 = float(input("Ingrese la longitud del primer lado más corto: "))
        lado2 = float(input("Ingrese la longitud del segundo lado más corto: "))
        print("La longitud de la hipotenusa es:", calcular_hipotenusa(lado1, lado2))
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
