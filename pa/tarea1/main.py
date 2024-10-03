from calculadora import Suma
from calculadora import Resta
from calculadora import Multiplicacion
from calculadora import Division
from calculadora import Exponencial


def main():
    
    while True:
        print("Selecciona la operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Exponencial")
        print("6. Salir")
        
        opcion = input("Elige una opción (1-6): ")
        
        if opcion == '6':
            print("Saliendo de la calculadora.")
            break

        num1 = float(input("Introduce el primer número: "))
        
        
        if opcion == '5':
            num2 = float(input("Introduce el exponente: "))
        else:
            num2 = float(input("Introduce el segundo número: "))

        if opcion == '1':
            operacion = Suma()
        elif opcion == '2':
            operacion = Resta()
        elif opcion == '3':
            operacion = Multiplicacion()
        elif opcion == '4':
            operacion = Division()
        elif opcion == '5':
            operacion = Exponencial()
        else:
            print("no valido")
            continue

        resultado = operacion.operar(num1, num2)
        print(f"El resultado es: {resultado}")
        

if __name__ == "__main__":
    main()