# Apartment Management API

A Django REST Framework backend for managing apartments, units, payments, notices, and maintenance requests with role-based access (landlord, caretaker, tenant).

## Features
- JWT authentication + DRF browsable API login
- Role-based permissions
  - Landlords: manage units, payments, notices, maintenance
  - Caretakers: manage payments, notices, maintenance
  - Tenants: create maintenance requests; read-scoped data
- Swagger/OpenAPI docs (`/api/docs/`) and ReDoc (`/api/redoc/`)

## Requirements
- Python 3.12+
- PostgreSQL 12+

## Quickstart

### 1) Setup environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2) Configure environment
Create a `.env` file in the project root with your settings:
```env
SECRET_KEY=replace-with-a-strong-secret
DEBUG=True

DATABASE_NAME=apartment_db
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=127.0.0.1
DATABASE_PORT=5432
```

### 3) Migrate database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4) Create a superuser (optional but recommended)
```bash
python manage.py createsuperuser
```

### 5) Run server
```bash
python manage.py runserver
```

Open:
- Home: http://localhost:8000/
- Admin: http://localhost:8000/admin/
- Browsable API auth (session): http://localhost:8000/api-auth/
- Swagger UI: http://localhost:8000/api/docs/
- ReDoc: http://localhost:8000/api/redoc/

## Apps and Models
- `users.User` (custom) — fields include `role` = `landlord|caretaker|tenant`
- `apartments.Unit` — `apartment_name`, `unit_number`, `floor`, `bedrooms`, `bathrooms`, `rent_amount`, `is_occupied`, `tenant`
- `payments.Payment` — `tenant`, `unit`, `amount`, `method`, `status`, `reference`, `paid_at`
- `notices.Notice` — `title`, `message`, `audience`, `recipient`, `created_by`
- `maintenance.MaintenanceRequest` — `unit`, `created_by`, `assigned_to`, `description`, `status`, `priority`

## Authentication
- JWT endpoints:
  - POST `/api/auth/login/` (get access/refresh)
  - POST `/api/auth/token/refresh/`
- Self registration (tenant only):
  - POST `/api/auth/register/`
- Add `Authorization: Bearer <ACCESS_TOKEN>` header for protected endpoints.

## Role-based Access Summary
- Units (`/api/apartments/units/`)
  - Read: authenticated users
  - Create/Update/Delete: landlord only
  - Tenants list only their assigned unit
- Payments (`/api/payments/payments/`)
  - Read: authenticated users
  - Create/Update/Delete: landlord or caretaker
  - Tenants list only their own payments
- Notices (`/api/notices/notices/`)
  - Read: authenticated users
  - Create/Update/Delete: landlord or caretaker
  - Tenants see `audience=all|tenants` and any direct `recipient`
- Maintenance Requests (`/api/maintenance/requests/`)
  - Read: authenticated users
  - Create: tenant
  - Update/Delete: landlord or caretaker
  - Tenants list only requests they created

## Filtering (query params)
- Units: `apartment_name`, `unit_number`, `is_occupied`, `tenant_id`
- Payments: `unit_id`, `status`, `method`, `tenant_id`
- Notices: `audience`, `created_by`, `recipient`
- Maintenance: `unit_id`, `status`, `priority`, `assigned_to`

## Example usage (cURL)

### Register tenant
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H 'Content-Type: application/json' \
  -d '{"username":"tenant1","email":"t1@example.com","password":"Passw0rd!","password2":"Passw0rd!"}'
```

### Login (JWT)
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H 'Content-Type: application/json' \
  -d '{"username":"tenant1","password":"Passw0rd!"}'
```
Response contains `access` and `refresh` tokens.

### Use token
```bash
ACCESS=replace-with-token
curl -H "Authorization: Bearer $ACCESS" http://localhost:8000/api/apartments/units/
```

### Create maintenance request (tenant)
```bash
curl -X POST http://localhost:8000/api/maintenance/requests/ \
  -H 'Authorization: Bearer '$ACCESS \
  -H 'Content-Type: application/json' \
  -d '{"unit": 1, "description": "Leaking sink"}'
```

## Development Notes
- Static files: The project references `STATICFILES_DIRS = [BASE_DIR / "static"]`. Create the folder or remove the setting to silence warnings.
- OpenAPI: Schema at `/api/schema/`, Swagger UI at `/api/docs/`, ReDoc at `/api/redoc/`.
- Default permissions: global DRF permission is `IsAuthenticated`. Public endpoints are explicitly opened (e.g., register, JWT auth).

## License
MIT (or your preferred license)
