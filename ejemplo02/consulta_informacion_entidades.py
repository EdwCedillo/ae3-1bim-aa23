"""
    Consulta de información en las entidades en la base de datos
"""

from base_datosEj02 import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute

# hace consultas a la base de datos de equipo
cadena_consulta_sql = "SELECT * from Equipo"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()

# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
print ("**EQUIPO**")
for d in informacion:
    print("%s - %s - %s - %d" % (d[0], d[1], d[2], d[3]))


# hace consultas a la base de datos de equipo
cadena_consulta_sql1 = "SELECT * from Jugador"
cursor.execute(cadena_consulta_sql1)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()

# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
print ("**JUGADOR**")
for d in informacion:
    print("%s - %s - %s - %d" % (d[0], d[1], d[2], d[3]))


# cerrar el enlace a la base de datos (recomendado)
cursor.close()
