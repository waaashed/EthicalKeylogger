# Keylogger Ethical

![Keylogger Image](https://moonlock.com/2023/09/Keylogger-analysis-header.png)

Ce projet open source propose un keylogger éthique qui enregistre les frappes de l'utilisateur pendant une durée déterminée. Les résultats sont ensuite présentés dans un rapport HTML interactif.

## Fonctionnalités

- **Enregistrement des frappes :** Capture les frappes de l'utilisateur.
- **Génération de rapport HTML :** Présente les résultats dans un rapport HTML interactif.
- **Webhook Discord :** Envoie les frappes au canal Discord spécifié.
- **Simulation réaliste :** Installation d'un faux programme Cisco.

## Comment utiliser

1. **Installation des dépendances :**
  ```bash 
  pip install -r requirements.txt
```
2. **Modification du code :**

```python
# Configuration
RECORD_DURATION = 10  # Temps en secondes
WEBHOOK_URL = "VOTRE API DISCORD WEBHOOK"  # Renseignez votre API
```

3. **Exécution du Keylogger :**

a. Assurez-vous d'avoir [Python](https://www.python.org/) installé sur votre machine.
  ```bash 

  python keylogger.py
```
4. **Installation et Utilisation avec Auto PY to EXE (Optionnel) :**

Auto PY to EXE est convertisseur de fichiers .py en .exe utilisant une interface graphique simple et PyInstaller en Python.

![pyinstaller](https://pypi-camo.freetls.fastly.net/eb29c9774b11dab42fbee0e2c5e9cf2af72895fc/68747470733a2f2f6e6974726174696e652e6e65742f706f7374732f6175746f2d70792d746f2d6578652f666561747572652e706e67)

a. Installation Via PyPI
```bash

  pip install auto-py-to-exe
```
b. Ensuite, pour l'exécuter, exécutez la commande suivante dans le terminal :
```bash

  auto-py-to-exe
```

## Avertissement
L'utilisation de keyloggers sans consentement est contraire à la vie privée et peut être illégale. Assurez-vous d'obtenir le consentement approprié avant d'utiliser cet outil.
