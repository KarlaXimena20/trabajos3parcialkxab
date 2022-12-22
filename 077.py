nombre1=input("Ingresa el nombre de alguien que quieras invitar a tu fiesta: ")
nombre2=input("Ingresa otro nombre: ")
nombre3=input("Ingresa un tercer nombre: ")
fiesta=[nombre1,nombre2,nombre3]
otro=input("¿Deseas invitar a alguien más? y/n ")
while otro == "y":
    nuevonombre=fiesta.append(input("Ingresa el nombre del invitado: "))
    otro=input("¿Deseas invitar a alguien más? y/n")
    print("Tienes", len(fiesta), "invitados")
    print(fiesta)
    seleccion=input("Ingresa uno de los nombres: ")
    print(seleccion, "está en la posición", fiesta.index(seleccion, "de la lista"))
    asistencia=input("¿Aún quieres que asista a tu fiesta? y/n")
    if asistencia == "n":
        fiesta.remove(seleccion)
        print(fiesta)

