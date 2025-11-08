# FastAPI Reservas Backend

## Overview

The FastAPI Reservas Backend is a web application designed to manage reservations for sports courts. It includes user authentication, court management, reservation handling, and feedback collection. The application is built using FastAPI, which provides automatic documentation through Swagger and Redoc.

## Features

- User registration and login with email and password
- Password hashing using bcrypt for security
- JWT token-based authentication for secure API access
- Automatic API documentation available at `/docs` (Swagger) and `/redoc` (Redoc)
- Modular architecture with clear separation of concerns

## Project Structure

The project is organized into several directories and files:

- **app/**: Contains the main application code.
  - **core/**: Core functionalities such as configuration and security.
  - **api/**: API routes and endpoints.
  - **models/**: Database models representing the application's data structure.
  - **schemas/**: Pydantic schemas for data validation and serialization.
  - **services/**: Business logic and service layer.
  - **utils/**: Utility functions for various tasks.
  
- **tests/**: Contains unit tests for the application.
- **requirements.txt**: Lists the dependencies required for the project.
- **.env.example**: Example environment variables for configuration.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **IMPLEMENTATION_PLAN.md**: Outlines the implementation plan for the project.
- **README.md**: Documentation for the project.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-reservas-backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up environment variables:
   - Copy `.env.example` to `.env` and fill in the necessary values.

## Running the Application

To start the FastAPI application, run the following command:
```
uvicorn app.main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

## API Documentation

- Swagger UI: `http://127.0.0.1:8000/docs`
- Redoc: `http://127.0.0.1:8000/redoc`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.