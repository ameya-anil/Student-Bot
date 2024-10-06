# Student Chatbot

A chatbot application built using Flask that initially collects student details and stores them in a file. After collecting enough data, the chatbot starts to respond to user queries regarding student information. The bot interacts with users through a web interface and provides answers based on the stored data.

## Features

- Collects student details like name, age, roll number, etc.
- Stores student details in a CSV file.
- Functions as a chatbot once a certain number of student details are collected.
- Responds to user queries for retrieving stored student information.
- Friendly responses for invalid or unrecognized queries.
- Beautiful web interface with a chatbox, styled using CSS.

## Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Data Storage:** CSV file

your_project/
├── app.py                # Main Flask application
├── templates/            # Folder for HTML files
│   └── index.html        # Chatbot interface
└── static/               # Folder for static assets like CSS and JS
    ├── style.css         # Styling for the interface
    └── script.js         # Chatbot JavaScript functionality
