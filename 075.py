nums=[123,345,678,890]
for i in nums:
    print(i)
seleccion=int(input("Introduzca un número de la lista: "))
if seleccion in nums:
    print(seleccion,"está en la posición",nums.index(seleccion))
else:
    print("No se encuentra en la lista")
