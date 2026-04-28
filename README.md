
# Nexus AI - Powered Customer Support Chatbot

![Project Banner](banner.png)

A senior-level web application demonstrating a Python and Flask-based chatbot. It leverages AIML for the conversational AI engine, stores conversation history in a MySQL database, and features a sleek, modern chat interface built with HTML, CSS, and vanilla JavaScript.

This project is designed to showcase a production-ready implementation, focusing on a clean architecture, separation of concerns, and a high-quality user experience, as would be expected in a senior developer role.

## 📱 Preview

![Chat Screenshot](screenshot.png)
*Nexus AI Chat Interface with simulated real-time response*

---

## ✨ Features

- **Conversational AI**: Core logic driven by AIML, allowing for an easily extendable knowledge base.
- **RESTful Backend**: A clean Flask API to handle chat messages and serve the frontend.
- **Database Persistence**: All conversations are saved to a MySQL database using SQLAlchemy for robust data management.
- **Modern UI/UX**: A polished, responsive chat interface that looks and feels like a real SaaS product. Includes dark mode support.
- **Scalable Architecture**: The project is structured with Flask Blueprints and an application factory pattern for maintainability and growth.
- **Secure Configuration**: Manages sensitive keys and database URIs via environment variables.

---

## 🛠️ Tech Stack

| Category   | Technology                                                                                                                                                             |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Backend**    | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![AIML](https://img.shields.io/badge/AIML-777777?style=for-the-badge)                                                                                                                                           |
| **Database**   | ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white) |
| **Frontend**   | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)         |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- MySQL Server
- `pip` for package management

### 1. Clone the Repository

```bash
git clone https://github.com/example/aiml-chat-assistant.git
cd aiml-chat-assistant
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root by copying the example file:

```bash
cp .env.example .env
```

Now, edit the `.env` file with your specific configuration:

```
FLASK_ENV=development
SECRET_KEY='a_very_secret_and_long_random_string'
DATABASE_URL='mysql+pymysql://YOUR_MYSQL_USER:YOUR_MYSQL_PASSWORD@YOUR_MYSQL_HOST/YOUR_DB_NAME'
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

1.  Ensure your MySQL server is running.
2.  Create a new database (e.g., `chatbot_db`).
3.  Use a MySQL client to execute the `schema.sql` file to create the necessary tables.

    ```sql
    -- Example using mysql CLI
    mysql -u YOUR_MYSQL_USER -p YOUR_DB_NAME < schema.sql
    ```

### 5. Run the Application

```bash
python app/main.py
```

The application will be available at `http://127.0.0.1:5000`.

---

## 📁 Project Structure

```
.env.example          # Environment variable template
README.md             # This file
requirements.txt      # Python dependencies
schema.sql            # Database table definitions

aiml_set/               # AIML knowledge base files
├── basic_chat.aiml
├── greetings.aiml
└── startup.xml

app/
├── static/             # Frontend assets
│   ├── css/style.css
│   └── js/main.js
├── templates/
│   └── index.html      # Main HTML page
├── __init__.py         # Flask application factory
├── aiml_kernel.py      # AIML engine setup and logic
├── config.py           # Configuration loader
├── main.py             # Application entry point
├── models.py           # SQLAlchemy database models
└── routes.py           # API and view routes
```

---

##  API Endpoint

### `POST /api/chat`

Handles the chat logic.

- **Request Body**:

```json
{
  "message": "Hello there!",
  "conversation_id": "some-uuid-string" // Optional
}
```

- **Success Response (200 OK)**:

```json
{
  "response": "Hello! How can I help you today?",
  "conversation_id": "some-uuid-string"
}
```

