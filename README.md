# 📘 Student Commute Optimizer

## 💡 Core Idea
The Student Commute Optimizer is a smart carpooling and route-sharing application designed specifically for students. It connects students traveling along similar paths, helping them share rides in an efficient, safe, and eco-friendly way. The system focuses on minimizing travel costs, reducing traffic congestion, and promoting sustainable commuting habits without compromising privacy.

## ✅ Solution

The solution consists of a student-friendly map interface where users input their start and end locations, view nearby students traveling along similar routes, and initiate chats with matched students under anonymized usernames. The backend processes route overlaps, traffic data, and user preferences to dynamically match students in real-time while ensuring data privacy. Additional features include eco-friendly routing suggestions, rerouting options in case of delays, and a gamification layer to encourage participation.

## High-level Architecture diagram
![alt text](image.png)

## ✅ Tech Stack

- *Frontend:* React.js with Tailwind CSS, OpenStreet Map API for visualization, WebSockets for real-time communication

- *Backend:* Node.js + Express.js, Python (for route optimization algorithms), Redis for caching frequent queries

- *Database:* MongoDB (for storing user data and pseudonyms securely)

- *Third-party APIs:* OpenStreet Map API(free), OpenWeather API, Traffic data providers

- *Authentication:* OAuth with anonymization layers