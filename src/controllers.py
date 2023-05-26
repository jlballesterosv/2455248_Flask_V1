from flask import render_template
from app import app

@app.route("/")
def index():
    return render_template('index.html', title="Inicio de Aplicativo")


@app.route("/lista-usuarios")
def lista_usuario():
    return render_template('lista-usuarios.html', title="Lista Usuarios")