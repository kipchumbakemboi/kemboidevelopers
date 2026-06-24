# Kemboi Developers & Consultancy

A full-stack Flask web application for **Kemboi Developers and Consultancy** — a modern technology and business solutions company based in Nairobi, Kenya.

> “Innovating Digital Solutions for a Better Tomorrow.”

## Project Structure

This is a complete production-ready structure including:

- Flask backend with SQLAlchemy
- User authentication (client, freelancer, admin roles)
- Portfolio management
- Blog CMS
- Quote request system
- Contact forms
- Admin dashboard
- M-Pesa payment integration (ready)
- AI chatbot integration (ready)

## Setup Instructions

1. **Clone or copy the project**

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Mac/Linux
   # or
   venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment**
   ```bash
   cp .env.example .env
   # Edit .env with your actual credentials
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. Visit `http://localhost:5000`

## Features Included

- Public website (Home, About, Services, Portfolio, Blog, Contact, Quote)
- User registration & login
- Role-based dashboards
- Admin panel for managing content
- Responsive modern UI
- Database models for all entities

## Next Steps / Extensions

- Add image upload functionality
- Implement full M-Pesa callback handler
- Integrate real AI API (OpenAI / Grok)
- Add email service integration
- Build the missing templates (blog/create, etc.)
- Add pagination and search

## Tech Stack

- Python + Flask
- SQLAlchemy + SQLite (easy to switch to PostgreSQL)
- Flask-Login
- Flask-Mail
- Bootstrap-ready styling

---

**Built by Kemboi Developers** — 2026
