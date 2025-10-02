from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap4
from flask_mail import Mail, Message
app = Flask(__name__)
bootstrap = Bootstrap4(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'jsolis@fi.uba.ar'
app.config['MAIL_PASSWORD'] = 'dcgo ccmy xbfp hmmq'
app.config['MAIL_DEFAULT_SENDER'] = 'jsolis@fi.uba.ar'
mail = Mail(app)

info_evento = {
    1: { 
        "nombre": "Evento de Ciclismo MTB Rural",
        "descripcion": "Te invitamos a sumarte a nuestro gran evento!! Comienza en:",
        "fecha": "24 de Octubre de 2025",
        "horario": "8:00 am",
        "lugar": "Tandil",
        "provincia": "Provincia de Buenos Aires",
        "auspiciantes": ["Mercado Libre","YPF", "Naranja X", "Claro", "Bet 365"]
        },
    2: {
        "redes_sociales": ["Twitter", "Facebook", "Instagram", "WhatsApp", "Correo Electrónico"]
        },
    3: {
        "parada": [1, 2, 3, 4, 5, 6, 7, 8],
        "recorridos": ["Parque Industrial Tandil", "Cerro Sagrada Familia", "Monolito Octavio J. Suarez", "Cruce Juan María", "Valle del Picapedrero", "Haras Santa Ana", "Aero Club Tandil", "Establecimiento Santa Marta"],
        "KM": [10, 20, 30, 40, 50, 60, 70, 80],
        "horario": ["0:45", "1:20", "2:10", "2:50", "4:00", "4:30", "5:30", "7:00"],
        "Punto_Hidrat": ["No", "No", "Sí", "No", "No", "Sí", "No", "Sí"]
        }
    }

@app.route("/registration.html", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        options = request.form["options"]
        elementos = "Sí" if request.form.get("elementos") else "No"

        msg = Message(
            subject=f"Inscripción Evento Ciclismo {name}",
            recipients=["jsolis@fi.uba.ar"],
            body=f"Yo, {name}, deseo inscribirme al Evento de Ciclismo, modalidad {options}.\n\n{message}\nElementos: {elementos}.\n\nSolicito la información a {email}."
        )
        mail.send(msg)
        return render_template("registration.html", success=True, name=name)
    return render_template('registration.html', info_evento=info_evento)

@app.route("/index.html")
def index():
    
    return render_template('index.html', info_evento=info_evento)



if __name__ == "__main__":
    app.run(debug=True)
