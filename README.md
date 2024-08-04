# BRAINS

Business Role-playing AI Network Simulation

## Overview

BRAINS is a FastAPI-based project designed with a modular structure. The project focuses on CRUD operations using JSON data instead of a traditional database. This setup facilitates easy and flexible data handling, suitable for various use cases, including simulations and role-playing scenarios.

## Project Structure

```
.
├── Dockerfile
├── LICENSE
├── README.md
├── init.py
├── app
│ ├── api
│ │ ├── init.py
│ │ └── v1
│ │ ├── init.py
│ │ ├── dependencies.py
│ │ └── endpoints
│ │ ├── init.py
│ │ └── example.py
│ ├── core
│ │ ├── init.py
│ │ ├── config.py
│ │ └── security.py
│ ├── data
│ │ └── example.json
│ ├── main.py
│ ├── schemas
│ │ ├── init.py
│ │ └── example_schema.py
│ ├── services
│ │ ├── init.py
│ │ └── example_service.py
│ └── utils
│ ├── init.py
│ └── common.py
├── data
├── directory_structure.txt
├── pytest.ini
├── requirements.txt
└── tests
├── init.py
└── test_example.py
```

## Project Modules

- app/api: Contains the API routes and endpoints.
- app/core: Holds the core configuration and security settings.
- app/data: Directory for storing JSON data files.
- app/main.py: The entry point of the FastAPI application.
- app/schemas: Contains Pydantic schemas for data validation.
- app/services: Provides the service layer for business logic.
- app/utils: Holds utility functions.
- tests: Contains test cases for the application.

## Endpoints

- GET /api/v1/: Retrieve all examples.
- POST /api/v1/: Create a new example.

## Example Usage

- GET /api/v1/:

```
curl -X 'GET' 'http://127.0.0.1:8000/api/v1/' -H 'accept: application/json'
```

- POST /api/v1/:

```
curl -X 'POST' 'http://127.0.0.1:8000/api/v1/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "test", "description": "test description"}'
```

## Additional Information

For more details, refer to the FastAPI and Pydantic documentation.

## License

This project is licensed under the terms of the LICENSE.