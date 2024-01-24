# Keylogger Ethical

![Keylogger Image](https://moonlock.com/2023/09/Keylogger-analysis-header.png)

Ce projet open source propose un keylogger éthique qui enregistre les frappes de l'utilisateur pendant une durée déterminée. Les résultats sont ensuite présentés dans un rapport HTML interactif.

## Fonctionnalités

- **Enregistrement des frappes :** Capture les frappes de l'utilisateur.
- **Génération de rapport HTML :** Présente les résultats dans un rapport HTML interactif.
- **Webhook Discord :** Envoie les frappes au canal Discord spécifié.
- **Simulation réaliste d'installation d'un programme Cisco.

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

3. **Exécution du Keylogger:**

a. Assurez-vous d'avoir [Python](https://www.python.org/) installé sur votre machine.
  ```bash 

  python keylogger.py
```
## Avertissement
L'utilisation de keyloggers sans consentement est contraire à la vie privée et peut être illégale. Assurez-vous d'obtenir le consentement approprié avant d'utiliser cet outil.
