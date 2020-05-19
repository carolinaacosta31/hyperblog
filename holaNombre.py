def hola_nombre(nombre, apellido):
    print(f'hola, {nombre} {apellido}')

def mensaje_multilinea():
    print('Platzi cuenta con cursos de: \n Desarrollo e ingeniería \n' 
    ' Negocios y emprendimiento \n Crecimiento profesional \n Desarrollo y UX')

if __name__ == '__main__':
    
    nombre = input('Cuál es tu nombre?')
    apellido = input('Cuál es tu apellido?')
    hola_nombre(nombre, apellido)
    mensaje_multilinea()
