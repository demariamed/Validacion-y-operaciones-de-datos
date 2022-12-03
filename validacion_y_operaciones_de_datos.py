# Validacion y operaciones de datos
# Aspirante: Consuelo de Maria Sanchez Medina
# C3 U Campers Python 
# Modulo 2

# Programa que identifica  la longitud de una palabra ingresada. La palabra correcta debe tener entre cuatro y ocho letras. 

id_usuario = input("Introduce el ID de usuario: ") # Se solicita id al usuario
if len(id_usuario) < 4 :
    print("Faltan caracteres. El ID debe contener entre 4 y 8 caracteres.", len(id_usuario)) # Si el ID es de menos caracteres informa cuántos faltan
elif len(id_usuario) > 8 :
    print("Sobran caracteres. El ID debe contener entre 4 y 8 caracteres.", len(id_usuario)) # Si el ID es de más caracteres informa cuántos sobran
elif len(id_usuario) >= 4 and len(id_usuario) <= 8:
    print("ID de usuario correcto") # Si el ID es correcto, informa que es correcto

#########################################################################################################################################################

# Crear un programa que en base a 2 números de entrada, coordenadas, identifique en cuál de los 4 cuadrantes se encuentra el punto. 
# El programa debe verificar que ninguna coordenada sea 0.

# Ingrese X: -5
# Ingrese Y: 8

# (X,Y): (+,+) => Cuad. I; (-,+) => Cuad. II; (-,-) => Cuad. III; (+,-) => Cuad. IV

print ('Bienvenido programa de verificacion de coordenadas')
x = int (input ('Ingresa el valor de x: ')) #int para hacerlo de tipo numerico
y = int (input ('Ingresa el valor de y: '))
if x==0 and y==0:
    print ('Origen')
if x>1 and y>1:
    print ('Cuadrante I') #Determina el rango del cuadrante 1
if x<-1 and y>1:
    print ('Cuadrante II') #Determina el rango del cuadrante 2
if x<-1 and y<-1:
    print ('Cuadrante III') #Determina el rango del cuadrante 3
if x>1 and y<-1:
    print ('Cuadrante VI') #Determina el rando del cuadrante 4
print ()

