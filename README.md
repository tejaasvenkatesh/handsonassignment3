# Django Terminal Chatbot

## Overview

This project is a terminal-based chatbot developed using **Python**, **Django**, and **ChatterBot**. The chatbot runs as a custom Django management command, allowing users to interact with it through the terminal. It uses a SQLite database to store conversation data and includes custom-trained responses for common user interactions.

## Features

- Terminal-based conversational chatbot
- Built with Django and Python
- Uses ChatterBot for AI-based responses
- Stores learned conversations in SQLite
- Includes custom conversation training
- Displays the current time upon request
- Supports graceful termination using `exit`, `quit`, or `bye`

## Project Structure

```text
django-terminal-chatbot/
│
├── chatbot_project/
├── terminalbot/
│   └── management/
│       └── commands/
│           └── chat.py
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

## Requirements

- Python 3.x
- Django
- ChatterBot
- ChatterBot Corpus

All required dependencies are listed in `requirements.txt`.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/django-terminal-chatbot.git
```

### 2. Navigate to the project directory

```bash
cd django-terminal-chatbot
```

### 3. (Optional) Create and activate a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

## Running the Application

Apply the Django migrations:

```bash
python manage.py migrate
```

Start the chatbot:

```bash
python manage.py chat
```

## Example Conversation

```text
user: Hello
bot: Hello! How can I help you today?

user: Good Morning
bot: Good morning! I hope you are having a great day.

user: How are you doing?
bot: I am doing great. Thank you for asking.

user: What is the time?
bot: The current time is 09:45 AM.

user: Thanks
bot: You are welcome.

user: Bye
bot: Goodbye. Have a great day!
```

## Manifest File

The project requires the following Python packages:

- Django
- ChatterBot
- ChatterBot Corpus

These dependencies are listed in the `requirements.txt` file.

## Technologies Used

- Python
- Django
- ChatterBot
- SQLite