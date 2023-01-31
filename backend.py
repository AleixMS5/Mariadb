import sys

import mariadb


def executarsentencia(sentencia):
    try:
        conn = mariadb.connect(
            user="ams",
            password="Almosa09",
            host="localhost",
            port=3306,
            database="proves"
        )
    except mariadb.Error as e:
        print(f"Error conectando a la base de datos: {e}")
        sys.exit(1)
    cur = conn.cursor()
    cur.execute(sentencia)
    conn.commit()

    conn.close()



def executarsentenciaSelect(sentencia):
    try:
        conn = mariadb.connect(
            user="ams",
            password="Almosa09",
            host="localhost",
            port=3306,
            database="proves"
        )
    except mariadb.Error as e:
        print(f"Error conectando a la base de datos: {e}")
        sys.exit(1)
    cur = conn.cursor()
    cur.execute(sentencia)
    conn.commit()
    pepe = cur.fetchall()
    conn.close()
    return pepe


def crearTaules():
    try:
        conn = mariadb.connect(
            user="ams",
            password="Almosa09",
            host="localhost",
            port=3306,
            database="proves"
        )
    except mariadb.Error as e:
        print(f"Error conectando a la base de datos: {e}")
        sys.exit(1)
    sentenciaSQL = """CREATE TABLE IF NOT EXISTS equipos
    ( idEquipo INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(40) NOT NULL,
    ciudad VARCHAR(40) NOT NULL,
    fundacion int NOT NULL,
    PRIMARY KEY (idEquipo),
    CONSTRAINT nombre_equipo UNIQUE (nombre)
    );
    """
    cur = conn.cursor()
    cur.execute(sentenciaSQL)
    conn.commit()

    sentenciaSQL = """CREATE TABLE IF NOT EXISTS jugadores
    ( idJugador INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(60) NOT NULL,
    posicion ENUM('Portero','Defensa central','Lateral izquierdo','Lateral derecho','Pivote','Mediocentro','Extremo izquierdo','Extremo derecho','Delantero centro'),
    nacimiento DATE,
    numero int NOT NULL,
    altura int NOT NULL,
    valorMercado int NOT NULL,
    idEquipo int NOT NULL,
    PRIMARY KEY (idJugador),
    CONSTRAINT fk_type
    FOREIGN KEY(idEquipo) 
        REFERENCES equipos(idEquipo));
    """
    cur = conn.cursor()
    cur.execute(sentenciaSQL)
    conn.commit()
