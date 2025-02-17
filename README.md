FastAPI User API

This project provides a simple FastAPI-based REST API to manage users. It includes the following endpoints:

Endpoints

1. Create a User (POST)

URL: /users/

Description: Adds a new user to the in-memory list.

Request Body: JSON object representing the user.

Response: Confirmation message and stored user data.

2. Get All Users (GET)

URL: /users/

Description: Retrieves the list of all stored users.

Response: JSON object containing all users.

Setup Instructions

Clone the repository:

git clone https://github.com/SirBauo/Trabajo_practico_2.git
cd your-repo

Install dependencies:

pip install -r requirements.txt

Run the application:

uvicorn main:app --reload

Access the API documentation at:

Swagger UI: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc
