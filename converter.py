menu = """
Bienvenido al conversor de monedas multipais

1-Pesos Mexicanos
2-Pesos Colombianos
3-Pesos Argentinos

Elige una opción: 

"""
opcion = int(input(menu))

if opcion == 1: 
	pesos = input('¿Cuántos pesos mexicanos tienes?: ')
	pesos = float(pesos)
	tipo_de_cambio = 21.5
elif opcion == 2: 
	pesos = input('¿Cuántos pesos colombianos tienes?: ')
	pesos = float(pesos)
	tipo_de_cambio = 3715.01
elif opcion == 3: 
	pesos = input('¿Cuántos pesos argentinos tienes?: ')
	pesos = float(pesos)
	tipo_de_cambio = 74.44
else:
	print('Escribe una opción correcta: ')



dolares = pesos / tipo_de_cambio
dolares = round(dolares, 2)
dolares = str(dolares)

print('Tienes $' + dolares +' dólares')



# menu = """
# Bienvenido al conversor de monedas💲

# 1-Pesos Colombianos
# 2-Pesos Mexicanos
# 3-Pesos Argentinos

# Elige una opcion
# """
# opcion = int(input(menu))
# if opcion == 1:
#     pesos = input("Cuantos pesos colombianos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar = 3875
#     dolares = pesos/valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dolares")
# elif opcion == 2:
#     pesos = input("Cuantos pesos mexicanos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar = 20.7
#     dolares = pesos/valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dolares")
# elif opcion == 3:
#     pesos = input("Cuantos pesos argentinos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar = 65
#     dolares = pesos/valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dolares")
# else:
#     print('Elige una opcion correcta')