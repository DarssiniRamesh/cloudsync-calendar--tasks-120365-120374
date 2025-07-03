# Project Repository

This is the initial README file for the project.

## Backend Environment Variable Setup

The backend (FastAPI, SQLAlchemy) requires the following environment variables to connect to the PostgreSQL database:

Add these variables (or adjust defaults) in your `.env` file or set them in your environment:

- `POSTGRES_URL` — database host/address (e.g. `localhost` or remote)
- `POSTGRES_USER` — database username (e.g. `calendaruser`)
- `POSTGRES_PASSWORD` — database password
- `POSTGRES_DB` — database name (e.g. `calendardb`)
- `POSTGRES_PORT` — port (typically `5432`)

Example `.env`:
```
POSTGRES_URL=localhost
POSTGRES_USER=calendaruser
POSTGRES_PASSWORD=calendarpass
POSTGRES_DB=calendardb
POSTGRES_PORT=5432
```

These variables are loaded automatically at startup. **Do not commit .env files with real passwords.**