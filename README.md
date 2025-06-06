# 🗂TaskBoard — Django Task Management App

TaskBoard is a web application built with Django that allows users to create, edit, and delete tasks, leave comments, like comments, and filter tasks by priority

## 🔧 Features

- User registration, login, and logout
- User profile page
- Task creation, editing, and deletion
- Priority and state selection
- Comments on tasks

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vladultimate/Task-Tracker
   cd taskboard
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Visit the app**:
   ```
   http://127.0.0.1:8000/
   ```

