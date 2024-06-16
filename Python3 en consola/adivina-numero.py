import random as rd
rango1=int(input("Selecciona el rango que tendrá el numero a adivinar: será desde __"))
rango2=int(input("hasta__"))
naleatorio = rd.randint(rango1,rango2)
prediccion= 0
while prediccion != naleatorio:
    prediccion=int(input(f"Adivina el numero entre {rango1} y {rango2} "))
    if prediccion < naleatorio:
        print("lejos perro, mas mayor")
    if prediccion > naleatorio:
        print("te pasaste perro, mas menor")
    if prediccion == naleatorio:
        print("le achuntaste perro, el numero era ",naleatorio)
        break
