import mariadb
import sys

from backend import crearTaules, executarsentenciaSelect
from backend import executarsentencia

# Datos de conexión

crearTaules()
while True:
    print("1:Inserir a la bbdd equips de futbol\n2:Inserir a la bbdd jugadors")
    obcio = input()
    if obcio == "1":
        print("1:incerir\n2:mostrar\n3:modificar\n4:esborrar")
        obcioEquips = input();
        if obcioEquips == "1":
            while True:
                try:
                    print("digues el nom de l'equip")
                    nombreEquipo = input()
                    print("digues la ciutat de l'equip")
                    ciudadEquipo = input()
                    print("digues l'any de fundaacio de l'equip")
                    fundacionEquipo = input()
                    sentenciaSQL = f"""INSERT INTO equipos
                    (nombre, ciudad, fundacion)
                    VALUES
                    ('{nombreEquipo}','{ciudadEquipo}',{fundacionEquipo});
                    """
                    executarsentencia(sentenciaSQL)
                except:print("has introduit alguna dada malament")
                finally: break

        if obcioEquips == "2":
            while True:
                try:
                    sentenciaSQL = f"""select * from equipos;
                        """
                    resultados = executarsentenciaSelect(sentenciaSQL)

                    for i in resultados:
                        print(i)
                except:print("has introduit alguna dada malament")
                finally: break
        if obcioEquips == "3":
            while True:
                try:
                    print("digues la id del equip que vols modificar")
                    id = input()
                    print("digues el nom de l'equip")
                    nombreEquipo = input()
                    print("digues la ciutat de l'equip")
                    ciudadEquipo = input()
                    print("digues l'any de fundaacio de l'equip")
                    fundacionEquipo = input()
                    sentenciaSQL = f"""UPDATE
                    equipos
                    SET
                    nombre ='{nombreEquipo}',  ciudad = '{ciudadEquipo}' ,fundacion = '{fundacionEquipo}'
                    WHERE idEquipo={id}]"""
                    executarsentencia(sentenciaSQL)
                except:print("has introduit alguna dada malament")
                finally: break
        if obcioEquips == "4":
            while True:
                try:
                    print("digues la id del equip que vols eliminar")
                    id = input()
                    sentenciaSQL = f"""
                    DELETE FROM equips WHERE idEquipo={id}"""

                except:print("no pots borrar aquest equip perque te jugadors o l'equip que vols borrar no existeix")
                finally: break

    if obcio == "2":
        print("1:incerir\n2:mostrar\n3:modificar\n4:esborrar")
        obcioJugadors = input();
        if (obcioJugadors == "1"):
            while True:
                try:
                    nombreEquipo = input("digues l'equip del jugador")

                    sentenciaSQL = f"""SELECT idEquipo FROM equipos
                    WHERE nombre = '{nombreEquipo}';
                    """

                    resultado = executarsentenciaSelect(sentenciaSQL)
                    for equipo in resultado:
                        idEquipo  = equipo[0]


                    nombreJugador = input("digues el nom del jugador")
                    numeroJugador = input("digues el numero del jugador")
                    posicion = ""
                    while True:
                        posicion = input("""digues la posicio del jugador pot ser 
                           Portero
                           Defensa central
                           Lateral izquierdo
                           Lateral derecho
                           Pivote
                           Mediocentro
                           Extremo izquierdo
                           Extremo derecho
                           Delantero centro\n""")
                        if posicion == "Portero" or posicion == "Defensa central" or posicion == "Lateral izquierdo" or posicion == "Lateral derecho" or posicion == "Pivote" or posicion == "Mediocentro" or posicion == "Extremo izquierdo" or posicion == "Extremo derecho" or posicion == "Delantero centro":
                            break
                    nacimiento = input("digues la data de naixement yyyy-mm-dd")
                    altura = input("digues l'altura del jugador")
                    valorMercado = input("digues el valor de mercat")

                    sentenciaSQL = f"""INSERT INTO jugadores
                    (nombre, numero, idEquipo,posicion,nacimiento,altura,valorMercado)
                    VALUES
                    ('{nombreJugador}','{numeroJugador}',{idEquipo},'{posicion}','{nacimiento}','{altura}','{valorMercado}');
                    """
                    executarsentencia(sentenciaSQL)
                except :print("¡has introduit alguna dada malament")
                finally: break




        if obcioJugadors == "2":

            sentenciaSQL = f"""select * from jugadores;
                """
            resultados = executarsentenciaSelect(sentenciaSQL)

            for i in resultados:
                print(i)
        if obcioJugadors == "3":
            print("digues la id del jugador que vols modificar")
            id = input()
            nombreEquipo = input("digues l'equip del jugador")

            sentenciaSQL = f"""SELECT idEquipo FROM equipos
                                WHERE nombre = '{nombreEquipo}';
                                """

            resultado = executarsentenciaSelect(sentenciaSQL)
            for equipo in resultado:
                idEquipo = equipo[0]
            nombreJugador = input("digues el nom del jugador")
            numeroJugador = input("digues el numero del jugador")
            posicion = ""
            while True:
                posicion = input("""digues la posicio del jugador pot ser 
                   Portero
                   Defensa central
                   Lateral izquierdo
                   Lateral derecho
                   Pivote
                   Mediocentro
                   Extremo izquierdo
                   Extremo derecho
                   Delantero centro\n""")
                if posicion == "Portero" or posicion == "Defensa central" or posicion == "Lateral izquierdo" or posicion == "Lateral derecho" or posicion == "Pivote" or posicion == "Mediocentro" or posicion == "Extremo izquierdo" or posicion == "Extremo derecho" or posicion == "Delantero centro":
                    break
            nacimiento = input("digues la data de naixement yyyy-mm-dd")
            altura = input("digues l'altura del jugador")
            valorMercado = input("digues el valor de mercat")
            sentenciaSQL = f"""UPDATE
            jugadores
            SET
            nombre ='{nombreJugador}',  numero = '{numeroJugador}' ,idEquipo = '{idEquipo}',posicion='{posicion}',nacimiento='{nacimiento}',valorMercado='{valorMercado}'
            WHERE idjugador={id}"""
            executarsentencia(sentenciaSQL)

        if obcioJugadors == "4":
            print("digues la id del jugador que vols eliminar")
            id = input()
            sentenciaSQL = f"""
            DELETE FROM jugadores WHERE idJugador={id}"""

