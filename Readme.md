# OpenAI Preguntas y Respuestas
Este es un programa que utiliza la API de OpenAI para responder preguntas ingresadas por el usuario. La interfaz gráfica de usuario fue creada utilizando la biblioteca tkinter de Python.

# Requisitos
Para utilizar este programa, necesitas tener instalados los siguientes paquetes de Python:

1. Tkinter, el cual viene instalado conjuntamente con las nuevas versiones de Python, de lo contrario puede instalarse con la herramienta "pip".
2. Openai, la cual puede descargarse e instalarse con la herramienta "pip".

*Además, debes tener una clave de API de OpenAI para utilizar la API. Si aún no tienes una, puedes obtenerla en el sitio web de [OpenAI](https://openai.com/).*

# Uso
Para utilizar el programa, ejecuta el archivo openai_preguntas.py en tu terminal de comandos. Luego, ingresa tu pregunta en el campo de entrada de texto y haz clic en el botón "Enviar". La respuesta de OpenAI se mostrará en una ventana de mensaje.

# Notas adicionales
Este programa utiliza el modelo de lenguaje text-davinci-003 de OpenAI para generar respuestas. Si deseas utilizar otro modelo, puedes cambiar la línea correspondiente en la función enviar_pregunta().
