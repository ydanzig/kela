# 🧪 Task Board Automation Project
End-to-end UI automation framework with CI/CD integration, Allure reporting, and scalable test architecture.

![CI](https://github.com/ydanzig/kela/actions/workflows/ui-tests.yml/badge.svg)

UI automation framework built with **Python, Pytest, and Playwright**.  
Covers core flows: **login, tasks, urgent events, and event history**.

---

## 📐 Framework Design

The framework is implemented using the **Page Object Model (POM)** pattern.

### 📁 Project Structure

```

project-root/
│
├── pages/                 # Page Object Model (UI abstraction)
│   ├── base_page.py       # Common reusable UI actions
│   ├── login_page.py      # Login page logic
│   ├── dashboard_page.py  # Dashboard actions
│   └── maps/              # UI locators (selectors)
│       ├── login_map.py
│       └── dashboard_map.py
│
├── tests/                 # Test scenarios grouped by feature
│   ├── expected.py        # Expected values for validation
│   ├── test_login.py
│   ├── test_tasks.py
│   ├── test_urgent_events.py
│   └── test_event_history.py
│
├── utils/                 # Shared configuration and helpers
│   └── config.py
│
├── .github/               # CI/CD configuration
│   └── workflows/
│       └── ui-tests.yml   # GitHub Actions workflow
│
├── conftest.py            # Pytest fixtures and setup
├── pytest.ini             # Pytest configuration
├── requirements.txt       # Python dependencies
├── README.md
└── BUGS.md
```

### 🧠 Design Explanation

- **pages/**  
    Encapsulates UI interaction logic and business actions, abstracting low-level Playwright operations

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

## 🔄 CI/CD

The project includes a **GitHub Actions workflow** for automated UI test execution.

The pipeline is triggered on:
- Push to main / master / feature branches
- Pull requests
- Manual execution via "Run workflow"

### 🔧 Workflow Capabilities

- Installs application dependencies (`npm install`)
- Starts the application in the background (`npm run dev`)
- Waits for the application to be ready before test execution
- Sets up Python environment and installs test dependencies
- Installs Playwright browser (Chromium)
- Runs the full Pytest suite
- Generates Allure test results
- Uploads test artifacts:
  - `allure-results`
  - application logs (`app.log`)

Workflow file:
.github/workflows/ui-tests.yml

---
### 📊 Viewing Test Results

Allure results are uploaded as CI artifacts.

To view locally:
1. Download the `allure-results` artifact from the GitHub Actions run
2. Extract it
3. Run:

```bash
allure serve allure-results
```

This will open the Allure report in your browser.

**Note:** Requires Allure CLI installed locally.

---

## ✅ Test Coverage

The framework provides end-to-end coverage of core user flows, including functional validation, UI behavior, and state management.

---

### 🔐 Login

**Scenarios covered:**
- Successful login with multiple valid credential combinations (case sensitivity, formats)
- Validation errors (empty username/password, short password, whitespace inputs)
- Error message validation (exact match)
- Session transition: login → dashboard
- Logout flow

**Relevant tests:**
- `test_login_success`
- `test_login_validation_errors`
- `test_logout_success`  
(see `tests/test_login.py`)

---

### 📋 Tasks

**Scenarios covered:**
- Task creation (full data / required fields only)
- Default values validation (time, description)
- Duplicate task behavior (allowed)
- Task deletion
- Invalid input validation (empty / whitespace)
- Stress scenario (multiple tasks)

**Relevant tests:**
- `test_add_task_success`
- `test_add_task_with_default_optional_values`
- `test_add_duplicate_task_allowed`
- `test_add_task_with_invalid_name`
- `test_add_many_tasks`
- `test_delete_task`  
(see `tests/test_tasks.py`)

---

### 🚨 Urgent Events

**Scenarios covered:**
- Creation of urgent events (all types)
- Parametrized validation across event types and urgent flag
- Required field validation (event type)
- UI validation (type, time, description)
- Styling validation (urgent vs non-urgent)
- Deletion flows (single and multiple events)

**Relevant tests:**
- `test_add_attack_urgent_event_success`
- `test_add_urgent_event_displays_values_for_each_type`
- `test_add_urgent_event_without_type`
- `test_delete_urgent_event`
- `test_delete_all_urgent_events_one_by_one`
- `test_delete_one_of_multiple_urgent_events`  
(see `tests/test_urgent_events.py`)

---

### 📜 Event History

**Scenarios covered:**
- Opening history panel
- Empty state validation
- Logging of task and urgent events
- Order validation (latest first)
- Mixed events scenarios
- Persistence after deletion

**Relevant tests:**
- `test_open_events_history_success`
- `test_events_history_empty_state`
- `test_task_creation_adds_event_to_history`
- `test_urgent_event_creation_adds_event_to_history`
- `test_events_history_order_latest_first`
- `test_mixed_events_are_logged_in_history`
- `test_task_deletion_does_not_remove_event_from_history`
- `test_multiple_task_creations_add_multiple_events_to_history`
- `test_urgent_event_order_latest_first` (skipped - known bug)  
(see `tests/test_event_history.py`)

---

### 🧪 Test Types & Methodology

The framework applies multiple testing strategies:

- Positive tests – valid user flows  
- Negative tests – invalid inputs and validation handling  
- State tests – system behavior after sequential actions  
- Edge cases – boundary inputs (empty, whitespace, duplicates)  
- Stress tests – handling multiple entities  
- Parametrized tests – broad coverage with minimal duplication  

---

### ⚠️ Known Gaps (Covered by Tests)

Some scenarios are intentionally tested but currently fail due to product bugs:

- Urgent events not appearing in event history  
- Incorrect styling logic for urgent events  
- Missing validation for whitespace-only task names  

Known issues are marked using `xfail` to maintain CI stability while preserving defect visibility.

---

## 🐞 Bugs

See `BUGS.md` for full details
