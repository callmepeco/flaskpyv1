from flask import Flask, render_template

#starting flask

app = Flask(__name__)

#contrução da rota

@app.route('/')
def index():
    return return render_template('index.html')

if __name__== "__main__":
    app.run(debug=True)


