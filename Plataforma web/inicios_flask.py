from flask import Flask

# indicar si nuestro archivo es el archivo principal, sie el archivo es el principal su valor sera __main__
app = Flask(__name__)


if __name__ == '__main__':

    app.run()  # debug=True para que se reinicie el servidor automaticamente al guardar cambi
