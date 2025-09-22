class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda  
        self.productos = []  

    def agregar_producto(self, nombre, precio, cantidad):
        if precio <= 0 or cantidad <= 0:
            print("Error: El precio y la cantidad deben ser positivos.")
            return  

        
        nuevo_producto = {
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad
        }
        self.productos.append(nuevo_producto)  
        print(f"Producto '{nombre}' agregado")

    def vender_producto(self, nombre, cantidad_a_vender):
        for producto in self.productos:
            if producto['nombre'].lower() == nombre.lower():  
                if cantidad_a_vender <= 0:
                    print("Error: La cantidad debe ser un número positivo.")
                    return
            
                if producto['cantidad'] >= cantidad_a_vender:
                    producto['cantidad'] -= cantidad_a_vender  
                    print(f"Venta de {cantidad_a_vender} unidades de '{nombre}' a sido realizada.")
                    return  
                else:
                    print(f"Error: No hay suficiente en stock de '{nombre}'. Stock actual: {producto['cantidad']}")
                    return  
        print(f"Error: Producto '{nombre}' no encontrado en el inventario.")

    
    def mostrar_inventario(self):
        print(f"\n--- Inventario de la tienda '{self.nombre_tienda}' ---")
        if not self.productos:  
            print("El inventario está vacío. Agrega algunos productos.")
        else:
            for producto in self.productos:
                print(f"{producto['nombre']} - Precio: ${producto['precio']:.2f} - Cantidad: {producto['cantidad']}")
        print("-------------------------------------------------")

    def producto_mas_caro(self):
        if not self.productos:
            print("El inventario está vacío. No hay productos para comparar.")
            return

        producto_caro = max(self.productos, key=lambda p: p['precio'])
        
        print(f"El producto más caro es '{producto_caro['nombre']}' con un precio de ${producto_caro['precio']:.2f}.")



mi_tienda = InventarioTienda("Abarrotes Sasuke Uchiha")
while True:
    print("\n--- Menú de Opciones ---")
    print("1. Agregar un nuevo producto")
    print("2. Vender un producto")
    print("3. Ver el inventario completo")
    print("4. Consultar el producto más caro")
    print("5. Salir del programa")
    
    opcion = input("Elige una opción (1-5): ")

    if opcion == '1':
        nombre = input("Ingresa el nombre del producto: ")
        try:
            precio = float(input("Ingresa el precio del producto: "))
            cantidad = int(input("Ingresa la cantidad a agregar: "))
            mi_tienda.agregar_producto(nombre, precio, cantidad)
        except ValueError:
            print("Error: El precio o la cantidad deben ser números.")
            
    elif opcion == '2':
        nombre = input("Ingresa el nombre del producto a vender: ")
        try:
            cantidad = int(input("Ingresa la cantidad a vender: "))
            mi_tienda.vender_producto(nombre, cantidad)
        except ValueError:
            print("Error: La cantidad a vender debe ser un número entero.")
            
    elif opcion == '3':
        mi_tienda.mostrar_inventario()
        
    elif opcion == '4':
        mi_tienda.producto_mas_caro()
        
    elif opcion == '5':
        print("usted a salido del programa")
        break  
        
    else:
        print("Opción no válida, elige un número del 1 al 5.")