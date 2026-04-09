# 🐞 Known Issues / Bugs

## 1. Urgent Events Not Logged in History

**Description:**  
Urgent events are not added to the Event History (View Events section).

**Steps to Reproduce:**
1. Add an urgent event
2. Open "View Events"

**Expected Result:**  
Urgent event should appear in the event history

**Actual Result:**  
Urgent event does not appear

**Impact:**  
High – missing critical data in history tracking

---

## 2. Incorrect Red Styling Logic for Urgent Events

**Description:**  
Event color is determined only by the "urgent" checkbox and not by event type.

**Steps to Reproduce:**
1. Create an event with urgent checkbox enabled
2. Observe event styling

**Expected Result:**  
Only specific event types (e.g. RED events) should be styled accordingly

**Actual Result:**  
Any event marked as urgent is displayed in red

**Impact:**  
Medium – misleading UI behavior

---

## 3. No User Isolation (Shared Data Between Users)

**Description:**  
All users can see the same data (tasks/events/history).

**Steps to Reproduce:**
1. Login as User A
2. Create tasks/events
3. Login as User B
4. Observe data

**Expected Result:**  
Each user should see only their own data

**Actual Result:**  
All users share the same data

**Impact:**  
High – data privacy issue

---

## 4. No Validation for Task Name (Spaces Only)

**Description:**  
Tasks can be submitted with a name containing only spaces, without any validation error.

**Steps to Reproduce:**
1. Try to create a task with only spaces in Task Name ("   ")
2. Click Add

**Expected Result:**  
Validation error "Please fill out this field" should appear

**Actual Result:**  
No error message is displayed

**Impact:**  
Low – UI issue.

---

## 5. Data Loss When Clicking Outside Task Dialog

**Description:**  
Clicking outside the task creation dialog clears all entered data.

**Steps to Reproduce:**
1. Open task creation form
2. Fill in fields
3. Click outside the dialog

**Expected Result:**  
User should be warned OR data should be preserved

**Actual Result:**  
All entered data is lost

**Impact:**  
Medium – poor user experience (UX issue)

---