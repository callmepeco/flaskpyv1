from flask import Flask

#starting flask

app = Flask(__name__)

#contrução da rota

@app.route('/')
def index():
    return "Hello, World!"

if __name__== "__main__":
    app.run(debug=True)


