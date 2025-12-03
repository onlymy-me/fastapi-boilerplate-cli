# ui

A FastAPI boilerplate project generated with fastapi-boilerplate-cli.

## Setup

1. Install dependencies:
```bash
uv pip install -r requirements.txt
```

2. Run the development server:
```bash
uvicorn main:app --reload
```

3. Visit http://localhost:8000/docs for interactive API documentation

## Project Structure

```
ui/
├── app/
│   ├── __init__.py
│   ├── routers/          # API route handlers
│   ├── schemas/          # Pydantic models
│   ├── dependencies.py   # Shared dependencies
│   └── config.py         # Configuration
├── main.py               # Application entry point
├── requirements.txt      # Dependencies
└── pyproject.toml       # Project metadata
```

## Features

- ✅ FastAPI setup with proper structure
- ✅ Health check endpoint
- ✅ Environment variable configuration
- ✅ Pydantic models for data validation
- ✅ Router-based architecture
- ✅ Ready for uv and ruff
