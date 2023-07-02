# Ejercicios de Cadenas

# V1
nombre = input("Nombre: ")
numero = int(input("Numero entero: "))
print((nombre + "\n") * int(numero))

# V2
nombre1 = input("Nombre completo: ")
print(nombre1.lower() + " / " + nombre1.upper() + " / " + nombre1.title() + "\n")

# V3
nombre2 = input("Nombre: ")
print(nombre2.upper() + " tiene " + str(len(nombre2)) + " caracteres" + "\n")

# V4
telefono = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
print('El número de teléfono es: ', telefono[4:-3] + "\n")

# V5
frase = input("Introduce una frase: ")
print(frase[::-1] + "\n")

# V6
frase1 = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")
print(frase1.replace(vocal, vocal.upper()) + "\n")

# V7
correo = input("Introduce un correo electronico: ")
print(correo[:correo.find("@")] + "@ceu.es" + "\n")

# V8
precio = input("Precio del producto con dos decimales: ")
print(precio[:precio.find(".")], " dolares y ", precio[precio.find(".")+1:], " centavos." + "\n")

# V9
fecha = input("Introduce fecha de nacimiento en formato dd/mm/aaaa: ")
print("Dia", fecha[:2])
print("Mes", fecha[3:5])
print("Año", fecha[6:])
# V9.1
fecha1 = input("Introduce fecha de nacimiento en formato dd/mm/aaaa: ")
dia = fecha1[:fecha1.find("/")]
mesaño = fecha1[fecha1.find("/")+1:]
mes = mesaño[:mesaño.find("/")]
año = mesaño[mesaño.find("/")+1:]
print("Dia", dia)
print("Mes", mes)
print("Año", año)

#  V10
compra = input("Nombre los productos con coma: ")
print(compra.replace(",", "\n"))
# V10.1
print("\n".join(compra.split(",")))

# V11
producto = input("Nombre del producto: ")
precio1 = float(input("Precio unitario: "))
unidades = int(input("Cantidad de unidades: "))
print('{producto}: {unidades:1d} unidades x {precio:1.2f}€ = {total:1.2f}€ total'.format(producto=producto, unidades=unidades, precio=precio1, total=unidades * precio1))
