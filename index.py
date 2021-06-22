from flask import Flask, render_template #  Trae el framwork de Flask e importa su librería

app = Flask(__name__) #  Variable reutilizable para usar la librería de Flask

@app.route('/') #  Ruta para la pagina home
def home():  #  Función para mostrar la ruta a home.html
    return render_template('home.html') # Retorna el html de home

@app.route('/about') #  Ruta para la pagina about
def about(): #  Función para mostrar la ruta a about.html
    return render_template('about.html') # Retorna el html de about

if __name__ == '__main__': #  Condicional para ejecutar 
        app.run(debug=True) #  permite correr la pagina constantemente y no debes iniciar la pagina por comandos cmd

