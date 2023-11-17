from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import app

from Model.Usuarios import usuarios
from Model.Peliculas import peliculas
from Model.Salas import salas
from Model.Funciones import funciones
from Model.Asientos import asientos
from Model.Compras import compras
from Model.tickets import tickets


#Rutas
from rutas.Mainlogin import routes_mainlogin
from rutas.descripcion import routes_Descripcion
from rutas.Admin import routes_Admin
from rutas.Asientos import routes_asientos
from rutas.Ticket import routes_CTicket
from rutas.Acerca import routes_Acerca
from rutas.AdminCompras import routes_AdminC
from rutas.Adminfunciones import routes_AdminF

#Ubicacion rutas

app.register_blueprint(routes_Descripcion, url_prefix="/fronted")
app.register_blueprint(routes_CTicket, url_prefix="/fronted")
app.register_blueprint(routes_Acerca, url_prefix="/fronted")
app.register_blueprint(routes_AdminC, url_prefix="/fronted")
app.register_blueprint(routes_AdminF,url_prefix="/fronted")




#Ubicacion rutas
app.register_blueprint(routes_mainlogin, url_prefix="/fronted")
app.register_blueprint(routes_asientos,url_prefix="/fronted")
app.register_blueprint(routes_Admin, url_prefix="/fronted")


@app.route("/")
def index():
    titulo= "Pagina Princiapl"
    return render_template('/Main/IndexMainLogin.html', titles=titulo)




# Datos de la tabla de Editoriales
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    


