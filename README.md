#  Abbo AgentsAI — Intelligent Workflow Assistant for Enterprise Operations

> AI Agent for Email Automation • Task Management • Customer Support  
> **Track:** Enterprise Agents  
> **Developer:** Abdelkerim Ali Abbo  
> **Language:** Python (Gemini API)

![Nom de l'image](./src/img/AbboAI.jpg)
---

##  1. Overview

Modern businesses waste enormous time manually handling emails, customer support messages, and internal task creation. Employees must sort, summarize, prioritize, and respond to dozens of messages every day.

**Abbo AgentsAI** is an AI-powered enterprise workflow assistant that automates these repetitive processes using a **multi-agent architecture** combined with Google's **Gemini models**.

L’agent peut :

-  lire et ingérer des messages (emails, tickets, demandes)
-  classifier le type de message (email simple, tâche, support)
-  résumer les points clés
-  générer des tâches actionnables (JSON)
-  produire des réponses automatiques de support
-  enregistrer les résultats dans une mémoire à long terme

Résultat : moins de travail manuel, des réponses plus rapides et une meilleure organisation des flux internes.

---

##  2. Problem Statement

Les entreprises font face à plusieurs problèmes récurrents :

- tri manuel des emails  
- création de tâches lente et répétitive  
- support client en retard ou incohérent  
- priorisation des demandes difficile  
- surcharge d’information

Les employés perdent plusieurs heures par semaine sur ces actions répétitives, alors qu’un agent intelligent peut automatiser une grande partie du flux.

---

##  3. Solution: Abbo AgentsAI

**Abbo AgentsAI** automatise les workflows de communication d’entreprise grâce à plusieurs agents coordonnés :

-  **Email Intake Agent** → capture le message brut
-  **Classifier Agent** → détecte le type de message : `email | task | support`
-  **Analyzer Agent** → résume et extrait les informations importantes
-  **Task Agent** → génère des tâches structurées au format JSON lorsque c’est une demande de travail
-  **Support Agent** → rédige une réponse de support claire et professionnelle
-  **Action Agent** → produit un résultat final formaté (rapport ou réponse)
-  **Logger Agent** → stocke les résultats utiles dans une mémoire à long terme

---

##  4. Key Features (Kaggle Requirements)

Ce projet démontre plusieurs concepts clés demandés dans le Capstone :

### ✔ Multi-Agent System
- Plusieurs agents spécialisés (intake, classifier, analyzer, task, support, logger)
- Pipeline séquentiel clair (chaque agent a un rôle précis)

### ✔ Tools
- Outils personnalisés pour :
  - lire et transformer les messages
  - générer des résumés
  - construire des tâches structurées
  - produire des rapports lisibles

### ✔ Memory
- **Session / short-term memory** : passage d’information d’un agent à l’autre  
- **Long-term memory (Memory Bank)** : stockage des derniers résultats (par exemple dernier rapport généré)

### ✔ Context Engineering
- Résumés avant traitement
- Instructions de rôle (classifier, support, etc.)
- Catégorisation explicite des messages (`email`, `task`, `support`)

### ✔ Observability
- Logs en console indiquant :
  - le type de message détecté
  - les étapes du pipeline
  - la sortie finale

### ✔ Gemini Model Use
- Agents propulsés par **Gemini Flash**  
  → modèle utilisé : `models/gemini-flash-latest`

---

##  5. Architecture Diagram

![Nom de l'image](./src/img/Architecture.png)



## 6. Installation & Setup
1. Cloner le dépôt
git clone `https://github.com/Abdelkerim516/Abbo_Agents_AI.git`
cd `Abbo_Agents_AI`

2. Créer et activer un environnement virtuel (recommandé)
python3 -m venv venv
source venv/bin/activate  # sur Linux / macOS
# venv\Scripts\activate   # sur Windows (PowerShell ou CMD)

3. Installer les dépendances
pip install -r requirements.txt