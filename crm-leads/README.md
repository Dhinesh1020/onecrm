# CRM Leads API

This is a FastAPI-based project for managing leads in a CRM system. It includes CRUD operations for leads and integrates with MongoDB.

## Features
- Add, view, update, and delete leads
- MongoDB as the database
- Dockerized setup

## Setup Instructions
1. Build and run the project using Docker Compose:
   ```bash
   docker-compose up --build
   ```
2. Access the API at `http://localhost:8000`.
3. MongoDB runs on `localhost:27017`.

## Endpoints
- `POST /leads/`: Create a new lead
- `GET /leads/`: List all leads
- `GET /leads/{lead_id}`: Get a lead by ID
- `PUT /leads/{lead_id}`: Update a lead
- `DELETE /leads/{lead_id}`: Delete a lead
