# app.py
from flask import Flask, render_template, request
from motor import inferir_compatibilidad
from base import hechos_signos

app = Flask(__name__)

# Lista de signos disponible para el formulario
SIGNOS = sorted(hechos_signos.keys())


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        signo1 = request.form.get("signo1", "").strip().lower()
        signo2 = request.form.get("signo2", "").strip().lower()

        if signo1 and signo2:
            resultado = inferir_compatibilidad(signo1, signo2)

    return render_template("index.html", signos=SIGNOS, resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)
