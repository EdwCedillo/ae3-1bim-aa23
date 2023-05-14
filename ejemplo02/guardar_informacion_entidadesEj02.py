"""
    Guarda información en las entidades en la base de datos
"""

from base_datosEj02 import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute

# Crear una cadena que almacene la sentencia de ingreso de información de Equipo
# se recuerda los atributos: nombreEquipo, claseEquipo, pais, cantJugad

nombreEquipo = "Independiente del Valle"
claseEquipo = "A"
pais = "Ecuador"
cantJugadores = 25
cadena_sql = """INSERT INTO Equipo (nombreEquipo, claseEquipo, pais, cantJugadores) \
VALUES ('%s', '%s', '%s', %d);""" % (nombreEquipo, claseEquipo, pais, cantJugadores)


# ejecutar el SQL
cursor.execute(cadena_sql)
# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()


# Crear una cadena que almacene la sentencia de ingreso de información de Jugador
# se recuerda los atributos: nombre, apellido, rol en Campo, numero de Jugador

# cadena_sql1 = 'CREATE TABLE Jugador (nombre TEXT, apellido TEXT, rolCampo TEXT, \
#           numJugador INTEGER)'
nombre = "Andres "
apellido = "Barzallo"
rolCampo = "Defensa"
numJugador = 3
cadena_sql1 = """INSERT INTO Jugador (nombre, apellido, rolCampo, numJugador) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, rolCampo, numJugador)

# ejecutar el SQL
cursor.execute(cadena_sql1)

# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
