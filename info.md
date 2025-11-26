# Python Flask App - CI/CD Lab

This is a Python Flask application designed for learning and practicing Continuous Integration/Continuous Deployment (CI/CD) concepts using GitHub Actions.

## About This Application

This project is a simple Flask web application that demonstrates:
- Python Flask web framework
- Automated testing with pytest
- Code quality checks with flake8
- CI/CD pipelines using GitHub Actions

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

This will install Flask and any other necessary packages.

## Running the Application

To start the Flask application, use the following command:

```bash
python3 -m flask --app startup run
```

The application will be available at `http://127.0.0.1:5000/`

## Running Tests

To run the test suite, execute:

```bash
python -m pytest
```

For more verbose output:

```bash
python -m pytest -v
```

## Project Structure

- `hello_app/` - Main application package
- `tests/` - Test files
- `startup.py` - Application entry point
- `requirements.txt` - Python dependencies
- `.github/workflows/` - CI/CD pipeline configurations
