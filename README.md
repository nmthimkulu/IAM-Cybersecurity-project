IAM Cybersecurity Project
Overview

The IAM Cybersecurity Project is a Flask-based web application designed to demonstrate Identity and Access Management (IAM) principles. It provides secure user authentication, role-based access control, and a structured dashboard system for both regular users and administrators.
Features

    User Registration and Login with form validation

    Role-based dashboards: separate views for users and admins

    Secure password handling with hashing and validation utilities

    Database integration using SQLite (iam.db)

    Configurable settings via config.py

    Reusable templates with base.html for consistent UI

    Unit tests for authentication and models to ensure reliability

Project Structure

    app/ → Core application logic (routes.py, models.py, forms.py, utils.py)

    templates/ → HTML templates (login.html, register.html, dashboard.html, dashboard_admin.html)

    static/css/ → Styling (style.css)

    instance/ → Configuration and database (config.py, iam.db)

    tests/ → Unit tests (test_auth.py, test_models.py)

    run.py → Application entry point

    requirements.txt → Python dependencies

Setup Instructions

    Clone the repository into your local environment:
    git clone https://github.com/yourusername/IAM-Cybersecurity-project.git

    Navigate into the project folder:
    cd IAM-Cybersecurity-project

    Create and activate a virtual environment:

        On macOS/Linux: python -m venv venv && source venv/bin/activate

        On Windows: python -m venv venv && venv\Scripts\activate

    Install the dependencies listed in requirements.txt:
    pip install -r requirements.txt

    Run the application:
    python run.py

Purpose

This project serves as a learning and demonstration tool for:

    Implementing IAM concepts in web applications

    Practicing secure coding techniques in Flask

    Building confidence in authentication, authorization, and database-backed security systems

Future Improvements

    JWT authentication for token-based security

    OAuth2 integration for third-party login providers

    Audit logging for tracking user activity

    Multi-factor authentication (MFA) for enhanced security

    Role hierarchy expansion to support complex access rules

 Future Improvements

    JWT authentication for token-based security.

    OAuth2 integration for third-party logins.

    Audit logging to track user activity.

    Multi-factor authentication (MFA) for stronger security.

    Role hierarchy expansion for complex access rules.

