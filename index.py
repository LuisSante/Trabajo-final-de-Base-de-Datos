from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generar-venta')
def about():
    return render_template('generacion.html')

@app.route('/products')
def cana_pescar():
    return render_template('products.html')

if __name__ == '__main__':
    app.run(debug = True)