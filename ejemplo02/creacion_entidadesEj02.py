"""
    Crear entidades en la base de datos
"""

from base_datosEj02 import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute

# Crear una tabla denominada Equipo
# con atributos: nombreEq, claseEq, pais, cantJugad

cadena_sql = 'CREATE TABLE Equipo (nombreEquipo TEXT, claseEquipo TEXT, pais TEXT, \
            cantJugadores INTEGER)'

# ejecutar el SQL
cursor.execute(cadena_sql)


# Crear una tabla denominada Jugador
# con atributos: nombre, apellido, rol en Campo, numero de Jugador

cadena_sql1 = 'CREATE TABLE Jugador (nombre TEXT, apellido TEXT, rolCampo TEXT, \
            numJugador INTEGER)'

# ejecutar el SQL
cursor.execute(cadena_sql1)


# cerrar la enlace a la base de datos (recomendado)
cursor.close()
