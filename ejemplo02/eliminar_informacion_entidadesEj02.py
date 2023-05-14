"""
    Consulta de información en las entidades en la base de datos
"""

from base_datosEj02 import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute

# Crear una cadena que almacene la sentencia de ingreso de información
# se recuerda los atributos: nombre, apellido, cedula, edad


# Crear una cadena que almacene la sentencia de ingreso de información de Equipo
# se recuerda los atributos: nombreEq, claseEq, pais, cantJugad

nombreEquipo = "Barcelona"
claseEquipo = "A"
pais = "Ecuador"
cantJugadores = 40
cadena_sql = """INSERT INTO Equipo (nombreEquipo, claseEquipo, pais, cantJugadores) \
VALUES ('%s', '%s', '%s', %d);""" % (nombreEquipo, claseEquipo, pais, cantJugadores)

# ejecutar el SQL
cursor.execute(cadena_sql)



# Crear una cadena que almacene la sentencia de ingreso de información de Jugador
# se recuerda los atributos: nombre, apellido, rol en Campo, numero de Jugador

# cadena_sql1 = 'CREATE TABLE Jugador (nombre TEXT, apellido TEXT, rolCampo TEXT, \
#           numJugador INTEGER)'
nombre = "Andres Manzano "
apellido = "B"
rolCampo = "Delantero"
numJugador = 8
cadena_sql1 = """INSERT INTO Jugador (nombre, apellido, rolCampo, numJugador) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, rolCampo, numJugador)

# ejecutar el SQL
cursor.execute(cadena_sql1)


# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# hace consultas a la base de datos
cadena_consulta_sql = "SELECT * from Jugador"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()

# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
for d in informacion:
    print("%s - %s - %s - %d" % (d[0], d[1], d[2], d[3]))

print("-------------------------------------------------")
# inicio proceso de elminación
cadena = """DELETE from Jugador WHERE nombre='%s'""" % ("Andres Manzano")
cursor.execute(cadena)
conn.commit()


# hace consultas a la base de datos
cadena_consulta_sql = "SELECT * from Jugador"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()

# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
for d in informacion:
    print("%s - %s - %s - %d" % (d[0], d[1], d[2], d[3]))


# cerrar el enlace a la base de datos (recomendado)
cursor.close()