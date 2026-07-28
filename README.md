# VisionGuard AI: Intelligent Face Recognition Security System

## Project Overview

VisionGuard AI is a Python-based security system that performs real-time face recognition using computer vision techniques.

The system can identify authorized and unauthorized persons and generate alerts when an unknown person is detected.

The main goal of this project is to provide a simple AI-based security solution using face recognition technology.

---

## Features

### Real-time Face Recognition

Uses OpenCV and the LBPH (Local Binary Pattern Histogram) algorithm for face detection and recognition.

### Voice Alerts

When an unknown person is detected, the system generates a voice alert using pyttsx3.

### Mobile Notifications

Sends instant notification alerts to the user's mobile device using the Pushbullet API.

### Privacy Protection

Personal face data and API keys are protected using `.gitignore` to prevent sensitive files from being uploaded.

---

## Tools & Technologies Used

- Programming Language: Python 3.x
- Computer Vision: OpenCV (opencv-contrib-python)
- Notifications: Pushbullet API
- Text-to-Speech: pyttsx3
- Data Processing: NumPy

---

## How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/VisionGuard_AI.git
cd VisionGuard_AI
