def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero."

def main():
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    operacion = input("Elige una operación (1/2/3/4): ")

    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
    
    if operacion == '1':
        print(f"Resultado: {suma(numero1, numero2)}")
    elif operacion == '2':
        print(f"Resultado: {resta(numero1, numero2)}")
    elif operacion == '3':
        print(f"Resultado: {multiplicacion(numero1, numero2)}")
    elif operacion == '4':
        print(f"Resultado: {division(numero1, numero2)}")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
