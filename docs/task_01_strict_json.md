## Task 1: Strict JSON Gateway Implementation

### Objective
Engineer a robust API endpoint that ingests a POST payload representing a candidate's resume and strictly validates its schema prior to execution.

### Technical Requirements
- **Endpoint:** `POST /resume`
- **Payload Schema:** JSON object containing:
  - `name`: String (Non-empty)
  - `skills`: Array of strings (Minimum 1 item)
  - `years_of_experience`: Integer (Strictly positive)

### Constraints & Error Handling
The framework must natively offload schema validation. Any payload violating the data contract must be automatically intercepted at the API boundary, resulting in a `422 Unprocessable Entity` response. This response must contain precise diagnostic telemetry on the failed constraint, eliminating the need for manual validation logic.
