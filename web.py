import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from backend import executarsentenciaSelect, executarsentencia


class jugador:
    idJugador = 0
    nombre = ""
    posicion = ""
    nacimiento = "1990-01-01"
    numero = 0
    altura = ""
    valorMercado = 0
    idEquipo = 0

    def __init__(self):
        pass


def descarregaWeb():
    print("digues el link del equip que vols descarregar")
    url = input()

    url2='https://www.transfermarkt.es/sevilla-fc/startseite/verein/368'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = {'User-Agent': user_agent}

    req = urllib.request.Request(url, None, headers)
    with urllib.request.urlopen(req) as response:
        resposta = response.read().decode("utf-8")
    fitxer = open("jugadors.html", "wt")
    fitxer = open("jugadors.html", "wt", encoding="utf-8")
    fitxer.write(resposta)
    fitxer.close()


def llegirFitxer():
    fitxer = open("jugadors.html", "rt", encoding="utf-8")
    html = fitxer.read()
    fitxer.close()

    inici = html.find('<table class="items">')
    final = html.find('<div class="keys"')
    taula = html[inici:final]

    taula = taula.replace('class=rn_nummer', 'class="rn_nummer"')
    taula = taula.replace('&nbsp;', '')

    taula = taula.replace('class=tm-shirt-number', 'class="tm-shirt-number"')
    taula = taula.replace('&nbsp;', '')





    fitxer = open("taula.xml", "wt", encoding="utf-8")
    fitxer.write(taula)
    fitxer.close()


def carregarXML():
    tree = ET.parse("taula.xml")
    root = tree.getroot()
    llistajugadors = []
    # Numeros:
    for tr in root.iter('tbody'):
        for td in tr.iter('td'):
            for div in td.iter('div'):
                j1 = jugador()
                if div.text != "-":
                    j1.numero = div.text
                else:
                    j1.numero = 0
                llistajugadors.append(j1)
    # Noms:
    comptador = 0
    for tbody in root.iter('tbody'):
        for a in tbody.iter('a'):
            if a.text is not None:
                llistajugadors[comptador].nombre = a.text.strip()
                comptador += 1

    # Posició:
    comptador = 0
    for tbody in root.iter('tbody'):
        for table in tbody.iter('table'):
            for td in table.iter('td'):
                if td.text is not None:
                    valor = td.text
                    valor = valor.strip()
                    if len(valor) > 0:
                        llistajugadors[comptador].posicion = td.text.strip()
                        llistajugadors[comptador].posicion = llistajugadors[comptador].posicion.strip()
                        comptador += 1
                    else:
                        llistajugadors[comptador].posicion = ""


    comptador = 0
    for tbody in root.iter('tbody'):
        tsd = 0
        for td in tbody.iter('td'):

            j = td.get("class");

            if j == "zentriert":
                tsd += 1
                if td.text is not None:
                    valor = td.text
                    valor = valor.strip()
                    if len(valor) > 0 and tsd % 7 == 1:
                        pepe = td.text.strip().split(" ")[0].replace("/", "-")
                        pepe=pepe.split("-")[2]+"-"+pepe.split("-")[1]+"-"+pepe.split("-")[0]
                        llistajugadors[comptador].nacimiento = pepe
                        comptador += 1

    comptador = 0
    for tbody in root.iter('tbody'):
        tsd = 0
        for td in tbody.iter('td'):

            j = td.get("class");

            if j == "zentriert":
                tsd += 1
                if td.text is not None:
                    valor = td.text
                    valor = valor.strip()
                    if len(valor) > 0 and tsd % 7 == 3:
                        pepe = td.text.strip().split(" ")[0].replace(",", "").replace("m", "").replace("-", "169")
                        llistajugadors[comptador].altura = pepe
                        comptador += 1

    comptador = 0
    for tbody in root.iter('tbody'):
        tsd = 0
        for td in tbody.iter('td'):

            j = td.get("class");

            if j == "rechts hauptlink":
                tsd += 1
                if td.text is not None:
                    valor = td.text
                    valor = valor.strip()

                    pepe = td.text.strip()


                    if pepe.split(" ")[1]=="mil":
                        pepe=int(pepe.split(" ")[0].replace(",", "").replace("m",
                                                                                      "").replace(
                        "-", "169"))*1000

                    elif pepe.split(" ")[1] == "mill.":
                        pepe = int(pepe.split(",")[0].replace(",", "").replace("m",
                                                                               "").replace(
                            "-", "169")) * 1000000


                    llistajugadors[comptador].valorMercado = pepe
                    comptador += 1
    try:
        sentenciaSQL = f"""select * from equipos;
                           """
        resultados = executarsentenciaSelect(sentenciaSQL)

        for i in resultados:
            print(i)
    except:
        print("has introduit alguna dada malament")
    print("dona la id del equip al que vols afegir els jugadors")
    idEquipo=input()
    for j in llistajugadors:
        sentenciaSQL = f"""INSERT INTO jugadores
                            (nombre, numero, idEquipo,posicion,nacimiento,altura,valorMercado)
                            VALUES
                            ('{j.nombre}','{j.numero}',{idEquipo},'{j.posicion}','{j.nacimiento}','{j.altura}','{j.valorMercado}');
                            """
        executarsentencia(sentenciaSQL)
        print(j.numero)
        print(j.nombre)
        print(j.posicion)
        print(j.nacimiento)
        print(j.altura)
        print(j.valorMercado)
        print("\n")


descarregaWeb()
llegirFitxer()
carregarXML()
