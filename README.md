# 🐛 Bug Tracker / Issue Tracker (Jira-like)

A lightweight, high-performance **Bug & Issue Tracking System** built using **FastAPI** as part of a **2-week industry-grade internship project**.  
The application is inspired by tools like **Jira, Linear, and ClickUp**, focusing on clean backend architecture, secure authentication, and scalable API design.

---

## 🚀 Project Overview

This project provides a backend system that allows teams to:

- Organize work into projects  
- Create and manage bug reports, tasks, and feature requests  
- Assign tickets to projects  
- Track issue status (Kanban-ready)  
- Secure APIs using JWT authentication  
- Interact via clean, auto-documented REST APIs  

The project follows **real-world backend development practices** and is designed to be easily extendable with a frontend (React).

---

## 🧰 Tech Stack

### 🔹 Backend
- **FastAPI** – High-performance Python web framework
- **SQLAlchemy** – ORM for database interaction
- **SQLite** (development) – Easily switchable to PostgreSQL
- **JWT Authentication** – Secure access control
- **Pydantic** – Data validation and serialization
- **Uvicorn** – ASGI server

### 🔹 Tooling
- **Swagger UI** – Interactive API documentation
- **Passlib (bcrypt)** – Secure password hashing
- **Python-JOSE** – JWT token handling

---

## 📂 Project Structure

bug_tracker_backend/
│
├── app/
│ ├── main.py # App entry point
│ ├── database.py # Database configuration
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── auth.py # JWT & password utilities
│ ├── dependencies.py # Auth & DB dependencies
│ │
│ ├── routers/
│ │ ├── auth.py # Authentication routes
│ │ ├── projects.py # Project APIs
│ │ └── tickets.py # Ticket APIs
│
├── requirements.txt
└── README.md


---

## 🔐 Authentication Flow

- User registers with email & password
- Passwords are securely hashed using **bcrypt**
- User logs in to receive a **JWT access token**
- Protected routes require a valid JWT token

---

## 📌 Core Features

### ✅ User Authentication
- Register & Login
- JWT-based secure authentication

### ✅ Project Management
- Create projects
- View user-owned projects

### ✅ Ticket Management
- Create tickets under projects
- View tickets by project
- Ticket statuses (Kanban-ready)

### ✅ API Documentation
- Auto-generated Swagger UI at `/docs`

---

## ▶️ Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/bug-tracker-backend.git
cd bug-tracker-backend
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Server
uvicorn app.main:app --reload
5️⃣ Open API Docs
http://127.0.0.1:8000/docs
🧪 API Testing
All APIs can be tested using Swagger UI:

Register user → /auth/register

Login → /auth/login

Create Project → /projects/

Create Ticket → /tickets/{project_id}
```
🔑 Authorization:
Use Bearer <your_token> in Swagger’s Authorize button.

📦 Future Enhancements
Role-based access control (Admin, Developer, Viewer)

Kanban drag-and-drop board (React)

Ticket comments & attachments

WebSocket-based real-time updates

PostgreSQL production database

Deployment using Railway / Fly.io

🧠 Learning Outcomes
Clean FastAPI project structuring

Secure JWT authentication

ORM-based relational data modeling

REST API design best practices

Real-world backend workflow

Screenshots: 

![WhatsApp Image 2026-02-05 at 12 53 35 PM (1)](https://github.com/user-attachments/assets/208bdcd9-1f4d-4e0d-8a29-7a4ae4052caf)



👨‍💻 Author
Tarun Tapan Tripathy
Python Developer Intern
B.Tech – Computer Science Engineering

⭐ Acknowledgements

Inspired by modern issue tracking platforms like Jira, Linear, and ClickUp, and built as part of an industry-oriented internship project.

