# 🧪 Task Board Automation Project

UI automation framework built with **Python, Pytest, and Playwright**.  
Covers core flows: **login, tasks, urgent events, and event history**.

---

## 📐 Framework Design

The framework is implemented using the **Page Object Model (POM)** pattern.

### 📁 Project Structure

```
project-root/
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── maps/
│       ├── __init__.py
│       ├── login_map.py
│       └── dashboard_map.py
│
├── tests/
│   ├── __init__.py
│   ├── expected.py
│   ├── test_login.py
│   ├── test_tasks.py
│   ├── test_urgent_events.py
│   └── test_event_history.py
│
├── utils/
|   ├── __init__.py
│   └── config.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── BUGS.md
```

### 🧠 Design Explanation

- **pages/**  
  Contains UI interaction logic only (clicks, inputs, reads)

- **tests/**  
  Contains business scenarios and assertions  
  Each file represents a feature

- **utils/**  
  Shared configuration (e.g. constants, test data)

- **expected.py**  
  Centralized expected values for validation

### Why this approach?

- Separation of concerns  
- High readability (tests describe behavior)  
- Reusability of actions  
- Easy maintenance when UI changes  

---

## ⚙️ Installation

### Run the application

```
npm install
npm run dev
```

Application URL:  
http://localhost:5173  

⚠️ Make sure the application is running before executing tests.

---

### Setup test environment

```
python -m venv .venv
```

Activate:

**Windows**
```
.venv\Scripts\activate
```

**Mac/Linux**
```
source .venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
playwright install chromium
```

---

## ▶️ Running Tests

Run all tests:

```
pytest
```

Run a specific test:

```
pytest .\tests\test_tasks.py::test_add_task_with_invalid_name
```

Verbose mode (more detailed output):

```
pytest -v
```

Headed mode (opens browser):

```
pytest --headed
```

Example:

```
pytest .\tests\test_tasks.py::test_add_task_with_invalid_name -v --headed
```

Stop on first failure:

```
pytest -x
```

---

## 📊 Reports (Allure)

Generate results:

```
pytest --alluredir=allure-results
```

Open report:

```
allure serve allure-results
```

💡 This will open a visual dashboard with:
- test results (pass/fail)
- execution steps
- error details
- timeline

---

## ✅ Coverage

- **Login** – success, validation, logout  
- **Tasks** – create, delete, duplicates, stress, negative  
- **Urgent Events** – create, validation, delete  
- **Event History** – logging, order, persistence  

---

## 🐞 Bugs

See `BUGS.md`
