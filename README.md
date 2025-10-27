# Email Scrapper System

## 🎯 Project Overview

An automated email scraping and classification system designed for IIT Gandhinagar's insIIT platform. The system periodically fetches emails, classifies them into categories, and stores structured data for various campus services.

## ✨ Features

- **Automated Email Fetching**: Scrapes new emails every 5 minutes
- **Multi-Category Classification**: Events, Mess Menu, Medical Updates, Opportunities, Timetables
- **Non-AI Pre-filtering**: Rule-based filtering to remove irrelevant emails
- **Structured Data Storage**: Follows predefined schemas for consistent data
- **Secure API Access**: Authentication-based REST API endpoints
- **Attachment Handling**: Extracts and processes email attachments

## 🎓 Use Cases

1. **Auto Event Updates**: Campus events and announcements
2. **Medical Unavailability**: Doctor schedules and availability
3. **Mess Menu Updates**: Daily meal schedules
4. **Timetable Updates**: Academic schedule changes
5. **Opportunity Updates**: Internships, jobs, scholarships

## 🏗️ System Architecture

```
Email Server (Gmail via IMAP)
         ↓
Email Access Module (OAuth2)
         ↓
Pre-Classifier (Rule-based)
         ↓
Email Parser Module
         ↓
AI/ML Classifier Module
         ↓
Database (MongoDB/SQL)
         ↓
REST API Service
```

## 💻 Tech Stack

- **Email Access**: Gmail API + OAuth2
- **Scheduler**: APScheduler / Celery
- **Backend**: Python (Flask/FastAPI)
- **Database**: MongoDB / PostgreSQL
- **Authentication**: JWT / OAuth2
- **API**: RESTful API

## 👥 Team Responsibilities

### Email Access Module
**Team Members**: Hardik, Satyam

**Responsibilities**:
- Implement OAuth2 authentication with Gmail
- Fetch new emails from IMAP server
- Extract email fields (from, to, subject, body, attachments)
- Handle email connection and session management

**Module Location**: `src/email_access/`

---

### Pre-Classifier Module
**Team Member**: Muder

**Responsibilities**:
- Create rule-based filtering logic
- Filter emails based on sender/subject patterns
- Remove spam and irrelevant emails
- Define filtering rules

**Module Location**: `src/pre_classifier/`

---

### Parser Module
**Team Members**: Ishani, Lakshika

**Responsibilities**:
- Parse email content and extract text
- Handle various email formats (HTML, plain text)
- Process and extract attachments
- Clean and normalize email content

**Module Location**: `src/parser/`

---

### Classifier Module
**Team Member**: Yashvardhan

**Responsibilities**:
- Categorize emails (events, mess, medical, opportunities)
- Format data according to predefined schemas
- Implement classification logic
- Validate classified data

**Module Location**: `src/classifier/`

---

### Database Module
**Team Member**: Arpit

**Responsibilities**:
- Design and implement database schema
- Create database models
- Implement CRUD operations
- Handle data persistence and retrieval
- Optimize database queries

**Module Location**: `src/database/`

---


## Contributing to Email Scrapper System


### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Email-Scrapper.git
cd Email-Scrapper
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix/MacOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt  # if available
```

## 🔄 Development Workflow

### 1. Create a Feature Branch

```bash
# Update main branch
git checkout main
git pull origin main

# Create feature branch
git checkout -b feature/your-module-name
```

### 2. Make Changes

- Work only in your assigned module directory
- Follow the code standards (see below)
- Write tests for your code
- Update documentation as needed

### 4. Commit Your Changes

```bash
git add .
git commit -m "feat(module-name): brief description"
```

### 5. Push and Create Pull Request

```bash
git push origin feature/your-module-name
```

Then create a Pull Request on GitHub.