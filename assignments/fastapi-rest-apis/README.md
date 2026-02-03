# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple RESTful API using the FastAPI framework to manage a small resource collection (books). Students will learn how to define Pydantic models, create CRUD endpoints, and run the app with `uvicorn`.

## 📝 Tasks

### 🛠️ Create the API

#### Description
Implement a FastAPI application that provides CRUD operations for a `Book` resource.

#### Requirements
Completed program should:

- Provide endpoints: `GET /books`, `GET /books/{id}`, `POST /books`, `PUT /books/{id}`, `DELETE /books/{id}`
- Use `pydantic` models for request/response validation
- Return appropriate HTTP status codes for success and errors
- Use an in-memory list as the data store (no database required)


### 🛠️ Run and Test

#### Description
Run the FastAPI app locally and verify the endpoints using `curl`, HTTP client, or a browser (Swagger UI).

#### Requirements

- Include instructions to run the app with `uvicorn`
- Provide example `curl` commands for each endpoint
- (Optional) Add simple tests using `pytest` or an HTTP client


### Starter Code

See `starter-code.py` in this folder for a minimal working FastAPI app to get you started.
