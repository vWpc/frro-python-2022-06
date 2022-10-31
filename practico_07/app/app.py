#PARA PODER HACER EL PRACTICO TUVIMOS QUE COPIAR DE LOS PRACTICOS ANTERIORES LOS ARCHIVOS Y PEGARLOS ACA
#TAMBIEN BORRAR LOS ASSERTS QUE PROVOCABAN ERRORES
#TUVIMOS QUE PONER EN LA CONEXION A LA BD connect_args={"check_same_thread": False} porque sino no andaba


#ENTENDI MAL LA CONSIGNA, HAY QUE METER LOS BOTONES ADENTRO DE LA TABLA


from flask import Flask,render_template,request,redirect,url_for,flash
from ejercicio_01 import Socio
from capa_negocio import NegocioSocio

app=Flask(__name__)
negocio=NegocioSocio()

@app.route('/')
def principal():    
    data=negocio.todos()
    return render_template('principal.html',data=data)

@app.route('/alta')
def pagalta():
    return render_template('pagalta.html')

@app.route('/altaenv', methods=['post'])
def altacontacto():
    dnialta=request.form['dnisocio']
    nombrealta=request.form['nombresocio']
    apellidoalta=request.form['apellidosocio']
    socio=Socio(dni=dnialta, nombre=nombrealta, apellido=apellidoalta)
    resultado = negocio.alta(socio)
    return redirect(url_for('principal'))
    
@app.route('/baja/<int:id_socio>')
def pagbaja(id_socio):
    baja= negocio.baja(id_socio)
    return redirect(url_for('principal'))    

@app.route('/modif/<int:id_socio>')
def pagmodif(id_socio):
    datasocio=negocio.buscar(id_socio)
    print(datasocio.dni)
    return render_template('pagmodificacion.html',data =datasocio)

@app.route('/modifenv', methods=['post'])
def modificarcontacto():
    dni=request.form['dnisocio']
    nombre=request.form['nombresocio']
    apellido=request.form['apellidosocio']
    socio=Socio(dni=dni, nombre=nombre, apellido=apellido)
    exito = negocio.modificacion(socio)
    return redirect(url_for('principal'))    

if __name__ == "__main__":
    app.run(debug=True,port=5000)