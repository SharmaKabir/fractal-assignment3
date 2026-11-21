# Smart Service Desk Management System

A Python CLI application for creating, viewing, searching, and resolving employee IT service requests. Request data persists in a JSON file so it remains available after the application restarts.

## Implemented Features

- Create a service request with an ID, employee name, issue, and priority
- Prevent duplicate Request IDs
- View all saved requests
- Search by Request ID
- Resolve an open request and persist the updated status
- Prevent resolving an already resolved request
- Safely load missing or empty JSON data
- Friendly handling for invalid priority and menu input

## Concepts Used

- **OOP:** `ServiceRequest` constructor, attributes, serialization, and `resolve()` behavior
- **Exception handling:** custom exceptions for duplicate IDs, missing requests, invalid priorities, invalid menu choices, and already resolved requests
- **File handling:** JSON loading and saving in `data/requests.json`
- **SOLID:** responsibilities are separated and `RequestService` depends on repository behavior rather than opening files itself
- **DDD:** domain, application, infrastructure, and presentation layers
- **Git:** development on `development`, testing, and merge into `main`

## Project Structure

```text
smart-service-desk/
├── domain/
│   ├── service_request.py
│   └── exceptions.py
├── application/
│   └── request_service.py
├── infrastructure/
│   └── file_repository.py
├── data/
│   └── requests.json
├── main.py
├── README.md
└── .gitignore
```

## Run the Application

From the project directory, run:

```bash
python main.py
```

Use the menu to create, view, search, and resolve service requests.

## Persistence Demonstration

1. Create `SR101` with priority `HIGH`.
2. Exit using menu option `5`.
3. Restart with `python main.py`.
4. Search for `SR101` and resolve it.
5. Exit and restart again; the resolved status will remain saved.

## Git Branch and Merge Workflow

Development was performed on the `development` branch using separate commits for project structure, domain model, JSON repository, application service, CLI, and documentation. After testing, `development` is merged into `main` and the final code is pushed to the remote repository.

```bash
git checkout main
git merge development
git push origin main
```