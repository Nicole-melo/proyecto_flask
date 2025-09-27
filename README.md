# Proyecto_Flask - Prototipo Educativo
Este proyecto es un prototipo de aplicación web desarrollado con **Flask (Python)** para demostrar el uso de plantillas dinámicas con **Jinja2** y buenas prácticas de modularidad.
Proyecto_Flask/
│── app.py
│── requirements.txt
│── Proyecto_Flask - FASE 0,I,II.docx
│
├── templates/
│ ├── base.html
│ ├── inicio.html
│ ├── servicios.html
│ ├── contacto.html
│ ├── header.html
│ ├── navbar.html
│ └── footer.html
│
├── static/
│ └── css/
│ └── style.css


---

## ⚙️ Cómo ejecutar el proyecto

1. Clonar este repositorio:
   ```bash
   git clone https://github.com/Nicole-melo/proyecto_flask.git
   cd proyecto_flask


Instalar dependencias:

pip install -r requirements.txt


Ejecutar la aplicación:

python app.py


Abrir en el navegador:

http://127.0.0.1:5000

🚀 Funcionalidades

Página Inicio con mensaje de bienvenida.

Página Servicios con lista de servicios.

Página Contacto con formulario que muestra confirmación.

Uso de plantilla base (base.html) y componentes reutilizables con include.
