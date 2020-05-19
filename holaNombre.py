def hola_nombre(nombre, apellido):
    print(f'hola, {nombre} {apellido}')

if __name__ == '__main__':
    
    nombre = input('Cuál es tu nombre?')
    apellido = input('Cuál es tu apellido?')
    hola_nombre(nombre, apellido)
