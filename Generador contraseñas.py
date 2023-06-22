#Generador de contraseñas: Desarrolla una aplicación que genere contraseñas seguras con diferentes criterios de complejidad.
import string
import random
import os

TEXTO = """
Generador de contraseñas 
Selecciona que tipo de contraseña deseas
1. Con una palabra clave.
2. aleatoria, con rango.
3. Sobre el programa.
4. Salir. 
Opción:  """
INFO = """
El programa 'Generador de contraseña' contiene 2 opciones claves 

1. Con una palabra clave.
      
Uno ingresa una cadena de texto y el programa desordenará el texto
dando asi una clave segura en base a lo que se ingrese. Se usó random.shuffle.

2. aleatoria, con rango.

Uno aquí puede seleccionar cuantas claves aleatorias quiere, ademas
de elegir cuantos digitos tendrán. Se usó la libreria random.

"""

while True:
        try:

            opcion=int(input(TEXTO))
            if opcion == 1:
                  os.system('cls')
                  palabra = input("Ingresa tu palabra clave: ")
                  listap = list(palabra)
                  random.shuffle(listap)
                  clave = ''.join(listap)
                  print("Tu nueva contraseña es:", clave)
                        
                            
            elif opcion==2:
                  os.system('cls')
                  number_of_strings = int(input("¿Cuantas contraseña generar? \n cantidad: "))
                  length_of_string = int(input("¿De cuantos digitos deseas? \n se recomienda mayor a 6 digitos: "))
                  
                  for x in range(number_of_strings):
                        print("Contraseña: ",''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
                
            elif opcion == 3:
                  os.system('cls')
                  
                  print(INFO)
                  

            
            
            elif opcion == 4:
                  print("Adios!")
                  break
        except ValueError:
              print("Ingresa una opcion correcta")

