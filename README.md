# 🧠 Cognitive Authenticity Engine  
### Behavioral Authorship Verification System

A real-time behavioral analytics system that evaluates writing authenticity using keystroke dynamics, temporal modeling, and statistical anomaly detection.

🔗 Live Demo: (https://cognitive-auth-engine-frontend.onrender.com/)  
🔗 Backend API Docs:(https://cognitive-auth-engine.onrender.com/docs)  

---

## 📌 Overview

The Cognitive Authenticity Engine is a full-stack behavioral verification system designed to evaluate whether a written response is organically authored by a candidate.

Unlike traditional AI detection systems that analyze final text output, this system analyzes the **writing process itself**.

It models how content is produced — not just what is produced.

The system generates a real-time:

Authenticity Score (0–100%)  
Risk Level: Low | Moderate | High  

---

## 🎯 Problem Statement

Text-based AI detection can be bypassed through:

- Rewriting AI-generated content  
- Paraphrasing  
- Re-typing generated answers  
- Using secondary devices  

Therefore, this system shifts focus from textual similarity to **cognitive-behavioral modeling**.

It evaluates behavioral consistency rather than output similarity.

---

# 🧠 Modeling Framework

The engine models writing behavior across four analytical layers:

---

## 1️⃣ Cognitive Process Modeling

Approximates cognitive effort and thought progression using:

- First Key Delay (response initiation latency)  
- Pause frequency  
- Maximum pause duration  
- Burst segmentation intervals  

Human writing typically exhibits irregular pauses and natural hesitation patterns.  
Externally assisted writing often shows unnatural initiation timing or structured bursts.

---

## 2️⃣ Behavioral Rhythm Modeling

Captures typing fingerprint characteristics:

- Mean inter-keystroke flight time  
- Flight time standard deviation  
- Typing rhythm irregularity  
- Baseline deviation using Z-score  

Human typing behavior contains natural noise and correction patterns.  
AI-assisted re-typing often exhibits smoother and more uniform rhythm segments.

---

## 3️⃣ Text Evolution Modeling

Models structural growth of written content:

- Incremental text expansion  
- Maximum text jump detection  
- Growth standard deviation  
- Content progression dynamics  

Human responses generally evolve gradually.  
Pasted or externally generated content often produces abrupt structural jumps.

---

## 4️⃣ Statistical Anomaly Modeling

Aggregates multi-signal inputs using:

- Baseline deviation scoring  
- Weighted anomaly aggregation  
- Threshold-based risk classification  
- Score normalization (0–100%)  

Final output:

Authenticity Score  
Risk Classification  

---

# 🏗️ System Architecture

Frontend (Render Static Site)  
        ↓  
FastAPI Backend (Render Web Service)  
        ↓  
PostgreSQL (Render Cloud Database)  
        ↓  
Feature Extraction Engine  
        ↓  
Statistical Scoring Model  

---

# ⚙️ Core Features

- Real-time keystroke tracking  
- Flight time variance analysis  
- Pause anomaly detection  
- Text growth jump detection  
- Baseline deviation modeling  
- Z-score behavioral comparison  
- Multi-signal risk aggregation  
- Animated authenticity visualization  
- Public cloud deployment  

---

# 📊 Behavioral Signals Extracted

- Mean Flight Time  
- Flight Time Standard Deviation  
- Pause Count  
- Maximum Pause  
- First Key Delay  
- Maximum Text Jump  
- Growth Standard Deviation  
- Baseline Z-Score  

These features are combined into a weighted authenticity scoring model.

---

# 🧪 Example Detection Scenarios

| Scenario | Behavioral Pattern | Risk Output |
|----------|-------------------|-------------|
| Gradual human typing | Natural pauses + edits | Low |
| Large pasted block | High text jump | High |
| Uniform burst typing | Reduced rhythm variance | Moderate |
| Long delay + sudden typing | Cognitive mismatch | Moderate/High |
| Baseline deviation | Statistical anomaly | Elevated |

---

# 🚀 Deployment

Fully deployed and publicly accessible.

### Backend
- FastAPI
- Uvicorn
- Hosted on Render Web Service

### Database
- PostgreSQL
- Hosted on Render Cloud Database
- Secure environment variable configuration (DATABASE_URL)

### Frontend
- Static site hosted on Render
- Real-time UI updates via Vanilla JavaScript
- SVG-based animated circular score visualization

---

# 🛠 Tech Stack

Backend:
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Uvicorn

Frontend:
- HTML
- CSS (Glassmorphism UI)
- Vanilla JavaScript
- SVG animations

Deployment:
- Render (Static Site + Web Service)
- Cloud PostgreSQL

---

# 💡 Engineering Challenges Solved

- Cloud PostgreSQL URL normalization  
- Environment variable configuration  
- Production deployment debugging  
- Real-time scoring synchronization  
- Smooth animated UI updates  
- Event-driven feature extraction  
- Baseline modeling within sessions  
- Multi-signal anomaly aggregation  

---

# 🔮 Future Enhancements

- Persistent cross-session behavioral fingerprinting  
- Isolation Forest anomaly detection  
- Keystroke entropy modeling  
- Backspace density tracking  
- Time-series visualization dashboard  
- Enterprise-grade assessment integration  

---

# 📸 Screenshots

(Add screenshots here)

Recommended:
- Normal typing session (Low Risk)
- Paste behavior (High Risk)
- Live dashboard animation

---

# 👨‍💻 Author

Yeruva Shanmukha Manohara Reddy  

GitHub: https://github.com/manoharreddyshanmukha  
LinkedIn: https://linkedin.com/in/manoharreddy369  

---

# 🏁 Outcome

This project demonstrates:

- Full-stack system design  
- Real-time behavioral analytics  
- Statistical anomaly modeling  
- Cloud-native deployment  
- Production debugging skills  
- Applied cognitive modeling  
- Engineering-level problem solving  
