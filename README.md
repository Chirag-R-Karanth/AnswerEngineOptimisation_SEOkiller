# Modern Full-Stack Signup & Login Application

This project is a modern, efficient web application featuring a light-themed, pleasant user interface. It is built with a React frontend and a FastAPI (Python) backend.

## Project Structure

- `frontend/`: React application scaffolded with Vite.
- `backend/`: Python backend powered by FastAPI.

## Tech Stack

### Frontend
- **React**: Modern UI library for efficient rendering.
- **Vite**: Ultra-fast build tool and development server.
- **Tailwind CSS v4**: Utility-first CSS framework for a "light and pleasant" design.
- **React Router**: For client-side navigation and redirection.
- **Axios**: For making API requests to the backend.

### Backend
- **FastAPI**: High-performance Python web framework for building APIs.
- **Uvicorn**: Lightning-fast ASGI server.
- **Pydantic**: Data validation using Python type annotations.

## Getting Started

### Prerequisites
- Node.js (v22 or higher)
- Python (v3.12 or higher)

### Installation

1.  **Frontend**:
    ```bash
    cd frontend
    npm install
    ```

2.  **Backend**:
    ```bash
    cd backend
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Start the Backend**:
    ```bash
    cd backend
    uvicorn main:app --reload --port 8000
    ```

2.  **Start the Frontend**:
    ```bash
    cd frontend
    npm run dev
    ```
    The application will be available at `http://localhost:5173`.

## Features

- **Clean & Light UI**: A pleasant, modern design using Tailwind CSS v4.
- **Signup & Login**: Fully functional authentication flow with automatic redirection to the main page upon success.
- **Fast Performance**: Built with high-performance frameworks on both ends.
- **Responsive Design**: Works across different screen sizes.
- **Verified Flow**: End-to-end flows verified with Playwright.
