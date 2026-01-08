# 🏏 Bowling Action Biomechanics Analysis System

An AI-based computer vision application that analyzes a cricket bowler’s action from video input and extracts key biomechanics metrics such as lean angle, head position, weight transfer, shoulder alignment, and release speed using pose estimation.

---

## 📌 Project Overview

This project allows a user to upload a bowling video and automatically:
- Detect the player’s skeletal posture
- Overlay the skeleton on the video
- Calculate biomechanical metrics frame-by-frame
- Display analysis results both inside the processed video and on the web interface

The system is designed for **sports performance analysis**, **injury prevention**, and **tech-assisted coaching**.

---

## 🎯 Features

- 🎥 Video upload via web interface  
- 🧍 Skeletal pose detection using computer vision  
- 📐 Lean angle calculation  
- 🧠 Head position detection  
- ⚖️ Weight transfer analysis  
- 💪 Shoulder alignment detection  
- 🚀 Release speed estimation  
- 🖍️ Real-time overlay of metrics inside video  
- 📄 Text-based analysis summary on webpage  

---

## 🛠️ Tech Stack

### Backend
- Java 21
- Spring Boot
- Maven
- REST APIs

### Computer Vision & AI
- Python
- OpenCV
- MediaPipe Pose

### Frontend
- HTML
- JavaScript (Fetch API)

### Tools
- Git & GitHub
- VS Code / IntelliJ IDEA

---

## 🧠 AI / ML Aspect

This project uses **pose estimation** (a computer vision AI technique) to detect human joint landmarks from video frames.  
Based on landmark positions, biomechanical angles and motion metrics are computed.

> ✔️ This is considered an **AI + Computer Vision project**, even though no deep learning model is trained manually.

---

## 📂 Project Structure

demobowling-analysis-backend/
│
├── src/main/java/
│ └── com/bowling/demobowlinganalysisbackend/
│ ├── controller/
│ │ ├── VideoUploadController.java
│ │ └── VideoStreamController.java
│ └── DemobowlingAnalysisBackendApplication.java
│
├── src/main/resources/
│ ├── static/
│ │ └── upload.html
│ └── analysis/
│ └── analysis.py
│
├── uploads/
│ └── processed videos
│
├── pom.xml
└── README.md

yaml
Copy code

---

## 🚀 How It Works

1. User uploads a bowling video from the web page
2. Spring Boot backend saves the video
3. Python analysis script runs automatically
4. Skeleton and metrics are overlaid on video
5. Processed video is saved
6. Analysis results are returned to the webpage

---

## ▶️ How to Run the Project

### Prerequisites
- Java 21 installed
- Python 3.9+
- Maven Wrapper (`mvnw`)
- Required Python libraries:
  ```bash
  pip install opencv-python mediapipe
Run Backend
bash
Copy code
.\mvnw spring-boot:run
Open Browser
bash
Copy code
http://localhost:9090/upload.html
📊 Output Metrics
Lean Angle (degrees)

Head Position (Left / Right / Stable)

Weight Transfer (Good / Poor)

Shoulder Alignment (Open / Closed / Neutral)

Release Speed (km/h equivalent estimation)

Overall Action Analysis

📈 Future Enhancements
Database integration (MySQL / PostgreSQL)

Player profile management

Graphs for run-up speed & shoulder rotation

Cloud deployment (AWS / Azure)

Mobile app support


👨‍💻 Author
Gowtham C
Electrical & Electronics Engineering
AI + Computer Vision Project
