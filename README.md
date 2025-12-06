# Waste Collection API

This project is a Flask-based web service that provides up-to-date information about waste collection locations. It serves as a backend for a mobile application, allowing users to find nearby waste collection points.

## Project Structure

```
waste-collection-api
├── app
│   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   └── collection_point.py
│   ├── routes
│   │   ├── __init__.py
│   │   └── api.py
│   ├── services
│   │   ├── __init__.py
│   │   └── collection_service.py
│   └── utils
│       ├── __init__.py
│       └── database.py
├── config
│   ├── __init__.py
│   └── config.py
├── tests
│   ├── __init__.py
│   └── test_api.py
├── requirements.txt
├── run.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd waste-collection-api
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```
   python run.py
   ```

## API Endpoints

- **GET /api/v1/version**
  - Returns the current version of the API.

- **GET /api/v1/locations**
  - Returns a list of waste collection locations.

## License

This project is licensed under the MIT License. See the LICENSE file for details.