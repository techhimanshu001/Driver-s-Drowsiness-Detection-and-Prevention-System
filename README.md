# Driver’s Drowsiness Detection and Prevention System

This project is a real-time Driver Drowsiness Detection and Prevention system developed using **OpenCV**, **HAAR Cascade classifiers**, and computer vision techniques. The system monitors the driver’s eye activity and triggers an alert if signs of drowsiness are detected, potentially preventing accidents caused by fatigue.

## 🔍 Project Overview

With the increasing number of road accidents due to driver fatigue and sleepiness, this system aims to:
- Detect drowsiness based on eye closure frequency
- Trigger an alarm or alert to wake the driver
- Reduce the risk of accidents on highways and long routes

It works in real-time using a webcam feed, continuously scanning facial landmarks, particularly the eyes, using HAAR cascades and facial detection models.

## 🛠️ Technologies Used
- Python
- OpenCV
- HAAR Cascade Classifiers
- dlib (optional for facial landmarks)
- NumPy

## 📌 How It Works
1. Capture real-time video using the webcam
2. Detect face and eye regions using trained classifiers
3. Track eye closure over time
4. If eyes remain closed for a certain threshold, trigger a buzzer or alert

## 📦 Future Scope
- Integration with IoT for vehicle control
- Adding fatigue score tracking over time
- Deploying in low-power embedded devices

## 🧪 Disclaimer
This is a prototype system developed for academic purposes only. Not intended for commercial use.
