# Maritime Operations & Compliance System

A full-stack web application for managing maritime ship operations, maintenance activities, safety drills, and compliance monitoring.

Built using:
- React + TypeScript
- Django REST Framework
- PostgreSQL
- JWT Authentication

---

# Features

## Authentication
- JWT-based login
- Protected routes
- Role-based access control

---

# Ship Management
- Create and manage ships
- Unique ship codes

---

# Maintenance Module
- Create maintenance tasks
- Assign tasks to crew
- Update task status:
  - Pending
  - In Progress
  - Completed
- Overdue task tracking

---

# Safety Drill Module
- Schedule drills
- Track drill participation
- Missed drill detection

---

# Compliance Dashboard
- Maintenance compliance %
- Drill compliance %
- Overall compliance %
- Overdue maintenance tracking
- Missed drill tracking

---

# Tech Stack

## Frontend
- React
- TypeScript
- Vite
- Axios
- React Router

## Backend
- Django
- Django REST Framework
- Simple JWT

## Database
- PostgreSQL

---

# Project Structure

```text
maritime-compliance-system/
│
├── backend/
│   ├── config/
│   ├── users/
│   ├── ships/
│   ├── maintenance/
│   ├── drills/
│   └── dashboard/
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── routes/
│   │   └── services/
│
└── README.md
