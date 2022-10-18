from flask import Flask,render_template,request,redirect,url_for
from ejercicio_01 import Socio

from capa_negocio import NegocioSocio

app=Flask(__name__)

@app.route('/')
def principal():
    negocio=NegocioSocio()
    data=negocio.todos()
    print('LO QUE SALE ES')
    print(data)
    return render_template('principal.html')

@app.route('/alta')
def pagalta():
    return render_template('pagalta.html')
@app.route('/altaenv', methods=['post'])
def altacontacto():
    print(request.form['dni'])
    print(request.form['nombre'])
    print(request.form['apellido'])
    return redirect(url_for('principal'))
    #negocio=NegocioSocio()
    #socio=Socio(dni=12345678, nombre='Juan', apellido='Lopez')
    #exito = negocio.alta(socio)
    #if exito:
    #    print ("Alta correcta")
    
    

if __name__ == "__main__":
    app.run(debug=True,port=5000)