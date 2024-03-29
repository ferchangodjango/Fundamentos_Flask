from flask import Flask,render_template,request,redirect,url_for

app= Flask(__name__)

@app.before_request
def before_request_action():
    print('La logica antes de realizar la petición se ejecuto correctamente')

@app.after_request
def after_request_action(response):
    print("Despues de la peticion")
    return response

@app.route('/')
def hello_world():
    lista_lenguajes=['Python','JavaScript','SQL','CSS']
    diccionario_prueba={
        'Titulo':'Ferchango_marango',
        'Saludos':'Que onda Crack',
        'Lenguajes':lista_lenguajes,
        'Numero_cursos':len(lista_lenguajes)
        }
    return render_template('index.html',data=diccionario_prueba)


#Pasando la variable desde la url(url dinamica) para que la refresque en el body de la pagina.
@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre,edad):
    data={
        'titulo':'contacto',
        'nombre':nombre,
        'edad':edad
        }
    return render_template('contacto.html',data=data)

#Obteniendo los valores desde la URL y tenerlos en la consola.
def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return "ok"

#Mostrando una vista para una pagina no encontrada
def pagina_no_encontrada(error):
    data={
        'titulo':'Pagina no encontrada',
        'Mensaje':'Uppsss... la pagina que buscas no existe'
    }
    #return render_template('Pagina_no_encontrada.html',data=data),404
    return redirect(url_for('hello_world'))

if __name__=='__main__':
    app.add_url_rule('/query_string',view_func=query_string)
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(debug=True,port=5000)

