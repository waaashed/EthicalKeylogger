# Keylogger

![Keylogger Image](https://moonlock.com/2023/09/Keylogger-analysis-header.png)

Ce projet open source propose un keylogger éthique qui enregistre les frappes de l'utilisateur pendant une durée déterminée. Les résultats sont ensuite présentés dans un rapport HTML interactif dans le but de sensibiliser les utilisateurs à l'exécution de logiciels tiers. La configuration du webhook Discord est facultative et ne pose pas de problème si elle n'est pas configurée. Elle sert uniquement de moyen d'identification.

## Fonctionnalités

- **Enregistrement des frappes :** Capture les frappes de l'utilisateur.
- **Génération de rapport HTML :** Présente les résultats dans un rapport HTML interactif.
- **Webhook Discord :** Envoie les frappes au canal Discord spécifié.
- **Simulation réaliste :** Installation d'un faux programme Cisco.
- **Indédectable :** ≈ 87% de réussite face à 70 Anti-Virus et 100% face aux Stations Blanches.

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

[Auto PY to EXE](https://pypi.org/project/auto-py-to-exe/) est convertisseur de fichiers .py en .exe utilisant une interface graphique simple et PyInstaller en Python.

![pyinstaller](https://s13.gifyu.com/images/S0BmI.gif)

a. Installation Via PyPI
```bash

pip install auto-py-to-exe
```
b. Ensuite, exécutez la commande suivante dans le terminal :
```bash

auto-py-to-exe
```
> [!WARNING]
> L'utilisation de keyloggers sans consentement est contraire à la vie privée et peut être illégale. Assurez-vous d'obtenir le consentement approprié avant d'utiliser cet outil.
