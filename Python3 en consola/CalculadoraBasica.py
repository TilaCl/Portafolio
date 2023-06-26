#Calculadora básica: Crea una calculadora que realice operaciones aritméticas simples.
print("Bienvenido a la calculadora aritmetica \n ")
a=int(input("Ingresa el numerador: "))
b=int(input("Ingresa el denominador: "))

suma = a+b
resta = a-b
mult = a*b
div =a//b
mensaje = f"""
Para los numeros {a} y {b},
La suma es {suma}.a
La resta es {resta}.
La multiplicacion {mult}.
La división {div}.


"""
print(mensaje)