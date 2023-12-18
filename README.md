# Keylogger Ethical

![Keylogger Image](https://moonlock.com/2023/09/Keylogger-analysis-header.png)

Ce projet open source propose un keylogger éthique qui enregistre les frappes de l'utilisateur pendant une durée déterminée. Les résultats sont ensuite présentés dans un rapport HTML interactif.

## Fonctionnalités

- **Enregistrement des frappes :** Capture les frappes de l'utilisateur.
- **Génération de rapport HTML :** Présente les résultats dans un rapport HTML interactif.
- **Webhook Discord :** Envoie les frappes au canal Discord spécifié.

## Comment utiliser

1. **Installation des dépendances :**
  ```bash 
  pip install flask pynput requests
```
2. **Modification du code :**

```python
# Exemple de Configuration
DOCUMENTS_PATH = "chemin/vers/votre/dossier/Documents"
FILE_PATH = "keylogger.txt"
RECORD_DURATION = 60 # Temps à changer à exprimer en secondes
WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_url"
```

3. **Exécution du Keylogger:**

a. Assurez-vous d'avoir [Python](https://www.python.org/) installé sur votre machine.
  ```bash 

  python keylogger.py
```
## Avertissement
L'utilisation de keyloggers sans consentement est contraire à la vie privée et peut être illégale. Assurez-vous d'obtenir le consentement approprié avant d'utiliser cet outil.
