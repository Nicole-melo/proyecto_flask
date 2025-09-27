from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "clave_secreta_demo"

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        correo = request.form.get("correo")
        mensaje = request.form.get("mensaje")

        if nombre and correo and mensaje:
            flash("Mensaje enviado correctamente ✅")
            return redirect(url_for("contacto"))
        else:
            flash("Por favor completa todos los campos ❌")

    return render_template("contacto.html")
    
if __name__ == "__main__":
    app.run(debug=True)
