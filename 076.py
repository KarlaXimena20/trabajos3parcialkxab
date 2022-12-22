nombre1=input("Ingresa el nombre de alguien que quieras invitar a tu fiesta: ")
nombre2=input("Ingresa otro nombre: ")
nombre3=input("Ingresa un tercer nombre: ")
fiesta=[nombre1,nombre2,nombre3]
otro=input("¿Deseas invitar a alguien más? y/n ")
while otro == "y":
    nuevonombre=fiesta.append(input("Ingresa el nombre del invitado: "))
    otro=input("¿Deseas invitar a alguien más? y/n")
    print("Tienes", len(fiesta), "invitados")

