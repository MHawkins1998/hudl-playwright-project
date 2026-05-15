# Hudl Playwright Automation

This project demonstrates an automated test framework built using Playwright with Python and pytest. The framework is designed to validate the Hudl login flow through a series of UI automation tests covering positive, negative, and navigation scenarios. The project follows standard automation practices using the Page Object Model (POM) design pattern and secure environment variable handling for test credentials.

# Technologies Used

- Python
- Playwright
- Pytest
- python-dotenv

## Framework Structure

- pages/
  -login_page.py

- tests/
  - test_login.py

Other Files:
- .env
- .gitignore
- README.md 

## Setup Instructions

### Clone the Repository

git clone <https://github.com/MHawkins1998/hudl-playwright-project>

### Create a Virtual Environment

```bash
python -m venv venv
```

#### Mac/Linux

```bash
source venv\bin\activate
```

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install playwright pytest python-dotenv
```

### Install Browsers

```bash
playwright install
```

## Environment Variables

Create a `.env` file in the project root directory and add the following credentials:

```env
HUDL_EMAIL=example@email.com
HUDL_PASSWORD=examplepassword
```

The `.env` file is excluded from version control using `.gitignore` to securely protect sensitive credentials.

## Running Tests

Ensure the environment is activated before running tests.

Run all tests:

```bash
python -m pytest
```

Run a specific test:

```bash
python -m pytest -k logout
```

## Test Coverage

This project currently tests:
- login page title verification
- login page url verification
- empty email validation
- empty password validation
- invalid login credentials
- forgot password navigation
- successful login
- logout functionality
