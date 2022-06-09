#############################################################################
# Seleccion De 1 o 2 (Se pueden agregar mas numeros al menu)
while True:
    print("1. manzana")
    print("2. pera")
    manorper = int(input("Seleccione el numero correspondiente: "))
    if manorper == 1 or manorper == 2:
        break
if manorper == 1:
    print ("Selecciono: Manzana")
else:
    print("Selecciono: Pera")
   
#############################################################################  
# Seleccion De palabras
while True: #Variable repetitiva
    manorper = str(input("Seleccione Manzana o Pera: ")) #Hacemos la selecion
    manorper = manorper.lower()#En caso de que el usuario use alguna mayuscula lo convertimos todo en minusculas
    if manorper == "manzana" or manorper == "pera": #Se busca la seleccion correspondiente (Se pueden agregar mas)
        break #Si se cumple rompera la seleccion
print ("Selecciono: ",manorper) #Muestra al usuario que escogio
