from flask import Flask

app= Flask(__name__)




#Request -> peticion
#response -> respuesta

@app.route('/')
def indedx():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')



if __name__ == "__name__":
    
    app.run()