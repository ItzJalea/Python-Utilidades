nombre = ""
while len(nombre) < 6: #Si el Nombre tiene menos de 6 caracteres se repetira
    nombre = input("Indique su nombre y apellido: ") #Esto pide el nombre y apellido del usuario
    if len(nombre) > 6: #Si el nombre tiene mas de 6 caracteres saldra del ciclo
        break
    print("Tu nombre y apellido deberia ser mas largo") # En caso de que el nombre no cumpla los requisitos mandara un mensaje
