from flask import Flask, request, app,make_response
from jinja2 import Environment, FileSystemLoader
from backend import executarsentenciaSelect


app = Flask(__name__)



@app.route('/')
def mostrar_equips():

    arrayequipos = []
    enviroment = Environment(loader=FileSystemLoader("templates/"))
    template = enviroment.get_template("plantillaLlistatEquips.html")
    sentenciaSQL=f"""SELECT * FROM equipos;"""
    resultados = executarsentenciaSelect(sentenciaSQL)
    for resultado in resultados:
        arrayequipos.append(
            {'id': resultado[0], 'nombre': resultado[1]});
    info = {"equip": arrayequipos}
    contingut = template.render(info)
    return f'{contingut}'


@app.route('/', methods=['GET', 'POST'])
def capturar_boto():

    if request.method == 'POST':
        arrayjugadores = []
        pepe="numero"
    if request.form.get('mostrarEquip')!=None:
        equip=request.form.get('mostrarEquip')
        resp = make_response()
        resp.set_cookie('equipo', request.form.get('mostrarEquip'))
        print( request.cookies.get('equipo'))
    else:
        equip = request.form.get('ordenar').split(",")[0]
    if (request.form.get('ordenar')!= None):
        pepe=request.form.get('ordenar').split(",")[1]

    equipGlobal = request.cookies.get('equipo')
    sentenciaSQL1 = f"""SELECT * FROM jugadores j, equipos e WHERE e.idEquipo = j.idEquipo and j.idEquipo={equip} order by j.{pepe};"""
    enviroment = Environment(loader=FileSystemLoader("templates/"))
    template = enviroment.get_template("plantilla.html")
    resultados = executarsentenciaSelect(sentenciaSQL1)
    for resultado in resultados:
        arrayjugadores.append(
            {'numero': resultado[4], 'nombre': resultado[1], 'posicion': resultado[2], 'naixement': resultado[3],
             'altura': resultado[5], 'valor': resultado[6], 'team': resultado[9],'id':resultado[7]})

    jocs = {"jocs": arrayjugadores}
    contingut = template.render(jocs)
    return f'{contingut}'





sentenciaSQL2 = f"""SELECT * FROM jugadores j, equipos e WHERE e.idEquipo = j.idEquipo and j.idEquipo=1 order by j.posicion;
              """
sentenciaSQL3 = f"""SELECT * FROM jugadores j, equipos e WHERE e.idEquipo = j.idEquipo and j.idEquipo=1 order by j.numero;
              """
sentenciaSQL4 = f"""SELECT * FROM jugadores j, equipos e WHERE e.idEquipo = j.idEquipo and j.idEquipo=1 order by j.nacimiento;
              """
sentenciaSQL5 = f"""SELECT * FROM jugadores j, equipos e WHERE e.idEquipo = j.idEquipo and j.idEquipo=1 order by j.altura;
              """

sentenciaSQL6 = f"""SELECT * FROM jugadores j, equipos e WHERE e.idEquipo = j.idEquipo and j.idEquipo=1 order by j.valorMercado;
              """




