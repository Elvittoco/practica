videojuegos = {

    "j001":["Minecraft","aventura","E"],
    "j002":["Resident evil","terror","M"],
    "j003":["Terraria","Aventura","E"],
    "j004":["Fifa 25","Deportes","E"],
    "j005":["Halo Ce","Disparos","M"]
}

inventario = {

    "j001":[25000,8],
    "j002":[42000,2],
    "j003":[8000,5],
    "j004":[38000,0],
    "j005":[39990,2]
}

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar videojuego")
    print("2. Buscar videojuego")
    print("3. Eliminar videojuego")
    print("4. Actualizar stock")
    print("5. Mostrar videojuegos")
    print("6. Salir")
    print("====================================")

def opcion_menu():
    while True:
        try:
            opcion = int(input("ingrese una opcion valida"))

            if opcion >=1 and opcion <= 6:
                return opcion
            else:
                print("la opcion ingresada es invalida")

        except ValueError:
            print("Debe ingresasr valores numericos, no letras")

#-------------------------- otros defs
def agregar_videojuego(videojuegos,inventario):
    
    codigo = input("Ingrese el codigo del video juego").lower().strip()

    if codigo in videojuegos:
        print("el codigo ya existe, intente otro codigo")
    else:

        nombre = input("Ingrese el nombre : ").strip()
        genero = input("ingrese genero del juego : ").strip()
        clasificacion = input("ingrese la clasificaicon del juego: ").upper().strip()

        while True:
            try:
                precio = int(input("Ingrese el precio del juego : "))
                stock = int(input("ingrese el stock del juego : "))
                break

            except ValueError:
                print("Debe ingresar solo numeros")

        videojuegos[codigo] = [nombre,genero,clasificacion]
        inventario[codigo] = [precio,stock]

def buscar_videojuego(videojuegos,inventario):

    codigo = input("Ingrese el codigo del juego que busca : ").lower().strip()

    if codigo in videojuegos:
        print("codigo :", codigo)
        print("nombre: ", videojuegos[codigo][0])
        print("Genero: ",videojuegos[codigo][1])
        print("clasificacion: ", videojuegos[codigo][2])
        
        print("precio", inventario[codigo][0])
        print("stock", inventario[codigo][1])

    else:
        print("El juego no existe")

def eliminar_videojuego(videojuegos,inventario):

    codigo = input("Ingrese el codigo del juego que desea eliminar : ").lower().strip()

    if codigo in videojuegos:

        videojuegos.pop(codigo)
        inventario.pop(codigo)

        print(" el juego a sido eliminado..")

    else:
        print("El video juego no existe, o ingreso mal los datos")

def actualizar_stok_videojuego(inventario):
    
    codigo = input("Ingrese el codigo del juego").lower().strip()

    if codigo in inventario:

        while True:
            try:

                nuevo_stok = int(input("Ingrese el nuevo stock del producto"))

                inventario[codigo][1] = nuevo_stok

                print("el stock a sido actualizado correctamente")
                break

            except ValueError:
                print("ingreso un caracter no valido")
            
    else: 
        print("juego buscado no existe")
    
def mostrar_videojuego(videojuegos,inventario):
    
    for codigo in videojuegos:
        print("-------------------------------")
        print("codigo : ",codigo)
        print("nombre : ",videojuegos[codigo][0])
        print("genero : ",videojuegos[codigo][1])
        print("clasificacion : ", videojuegos[codigo][2])
        print("precio : ", inventario[codigo][0])
        print("stock : ", inventario[codigo][1])


#------------------------- menu

while True:

    mostrar_menu()

    opcion_seleccionada = opcion_menu()

    if opcion_seleccionada == 1:
        agregar_videojuego(videojuegos,inventario)

    elif opcion_seleccionada == 2:
        buscar_videojuego(videojuegos,inventario)

    elif opcion_seleccionada == 3:
        eliminar_videojuego(videojuegos,inventario)
    
    elif opcion_seleccionada == 4:
        actualizar_stok_videojuego(inventario)

    elif opcion_seleccionada == 5:
        mostrar_videojuego(videojuegos,inventario)

    elif opcion_seleccionada == 6:
        print("Saliendo del programa...")
        break
