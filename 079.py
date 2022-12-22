nums=[]
total=0

while total>3:
    num=int(input("Ingresa un número: "))
    nums.append(num)
    print(nums)
    total=total+1
    ultimonum=input("Desea guardar el último número? y/n")
    if ultimonum == "n":
        nums.remove(num)
        print(nums)
