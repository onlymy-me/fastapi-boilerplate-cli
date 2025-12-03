"""
FastAPI Boilerplate Generator CLI
A tool to quickly scaffold FastAPI projects with best practices
"""

import sys
import os
from pathlib import Path





# Template files content
MAIN_PY = '''from fastapi import FastAPI
from app.routers import health

app = FastAPI(
    title="{project_name}",
    description="A FastAPI boilerplate project",
    version="0.1.0"
)

# Include routers
app.include_router(health.router)


@app.get("/")
def read_root():
    return {{"message": "Welcome to {project_name}"}}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
'''

HEALTH_ROUTER = '''from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/")
def health_check():
    return {"status": "healthy"}
'''

SCHEMAS_PY = '''from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
'''

DEPENDENCIES_PY = '''from typing import Generator


def get_db() -> Generator:
    """Database session dependency"""
    # TODO: Implement database session
    pass
'''

CONFIG_PY = '''import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "{project_name}"
    debug: bool = True
    api_v1_str: str = "/api/v1"
    
    class Config:
        env_file = ".env"


settings = Settings()
'''

ENV_TEMPLATE = '''# Environment variables
DEBUG=True
DATABASE_URL=sqlite:///./app.db
SECRET_KEY=your-secret-key-here
'''

REQUIREMENTS = '''fastapi==0.115.0
uvicorn[standard]==0.32.0
pydantic==2.9.0
pydantic-settings==2.6.0
'''

PYPROJECT_TOML = '''[project]
name = "{project_name}"
version = "0.1.0"
description = "A FastAPI boilerplate project"
requires-python = ">=3.8"
dependencies = [
    "fastapi>=0.115.0",
    "uvicorn[standard]>=0.32.0",
    "pydantic>=2.9.0",
    "pydantic-settings>=2.6.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.ruff]
line-length = 88
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I"]
'''

README = '''# {project_name}

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
{project_name}/
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
'''

GITIGNORE = '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv/
ENV/
build/
dist/
*.egg-info/
.pytest_cache/

# Environment
.env
.env.local

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
'''


def create_file(filepath: Path, content: str):
    """Create a file with the given content"""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(content, encoding="utf-8")
    print(f"✅ Created: {filepath}")


def generate_project(project_name: str, directory: str = "."):
    """Generate FastAPI project structure"""
    
    # Create base directory
    base_dir = Path(directory) / project_name
    if base_dir.exists():
        print(f"❌ Error: Directory '{project_name}' already exists!")
        sys.exit(1)
    
    base_dir.mkdir(parents=True)
    print(f"\n🚀 Creating FastAPI project: {project_name}\n")
    
    # Create app directory structure
    app_dir = base_dir / "app"
    app_dir.mkdir()
    
    # Create subdirectories
    (app_dir / "routers").mkdir()
    (app_dir / "schemas").mkdir()
    
    # Create __init__.py files
    create_file(app_dir / "__init__.py", "")
    create_file(app_dir / "routers" / "__init__.py", "")
    create_file(app_dir / "schemas" / "__init__.py", "")
    
    # Create main files
    create_file(base_dir / "main.py", MAIN_PY.format(project_name=project_name))
    create_file(app_dir / "routers" / "health.py", HEALTH_ROUTER)
    create_file(app_dir / "schemas" / "health.py", SCHEMAS_PY)
    create_file(app_dir / "dependencies.py", DEPENDENCIES_PY)
    create_file(app_dir / "config.py", CONFIG_PY.format(project_name=project_name))
    
    # Create config files
    create_file(base_dir / "requirements.txt", REQUIREMENTS)
    create_file(base_dir / "pyproject.toml", PYPROJECT_TOML.format(project_name=project_name))
    create_file(base_dir / ".env.example", ENV_TEMPLATE)
    create_file(base_dir / ".gitignore", GITIGNORE)
    create_file(base_dir / "README.md", README.format(project_name=project_name))
    
    # Success message
    print(f"\n✨ Successfully created '{project_name}'!\n")
    print("📦 Next steps:")
    print(f"   cd {project_name}")
    print("   uv pip install -r requirements.txt")
    print("   uvicorn main:app --reload")
    print("\n📚 Docs will be available at: http://localhost:8000/docs\n")


def show_help():
    """Show help message"""
    help_text = """
FastAPI Boilerplate Generator

Usage:
    fastapi-boilerplate create <project-name>      Create a new FastAPI project
    fastapi-boilerplate --help                     Show this help message

Examples:
    fastapi-boilerplate create my-api
    fastapi-boilerplate create awesome-backend
    
This will create a complete FastAPI project structure with:
    ✅ Main application file
    ✅ Router-based architecture
    ✅ Pydantic schemas
    ✅ Configuration management
    ✅ Environment variables support
    ✅ Ready for uv and ruff
"""
    print(help_text)


def main():
    """Main CLI entry point"""
    
    # Parse arguments
    args = sys.argv[1:]
    
    if len(args) == 0 or args[0] == "--help" or args[0] == "-h":
        show_help()
        sys.exit(0)
    
    if args[0] == "create":
        if len(args) < 2:
            print("❌ Error: Please provide a project name")
            print("Usage: fastapi-boilerplate create <project-name>")
            sys.exit(1)
        
        project_name = args[1]
        
        # Validate project name
        if not project_name.replace("-", "").replace("_", "").isalnum():
            print("❌ Error: Project name should only contain letters, numbers, hyphens, and underscores")
            sys.exit(1)
        
        generate_project(project_name)
    else:
        print(f"❌ Unknown command: {args[0]}")
        print("Use 'fastapi-boilerplate --help' for usage information")
        sys.exit(1)


if __name__ == "__main__":
    main()
