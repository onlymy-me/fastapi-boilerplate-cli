# FastAPI Boilerplate CLI

⚡ A simple CLI tool to generate FastAPI project boilerplates with best practices.

[![PyPI version](https://badge.fury.io/py/fastapi-boiler-cli.svg)](https://pypi.org/project/fastapi-boilerplate-cli/)

## Installation

```bash
uv tool install fastapi-boilerplate-cli
```

## Usage


# Create a new FastAPI project
```bash
fastapi-boilerplate create my-awesome-api
```
# Navigate to your project
```bash
cd my-awesome-api
```
# Install dependencies
```bash
uv pip install -r requirements.txt
``` 
or

```bash
uv add -r requirements.txt
```
# Run the server
```bash
uvicorn main:app --reload
```
Visit http://localhost:8000/docs for interactive API documentation!

## What Gets Generated

- ✅ FastAPI app with router-based architecture
- ✅ Health check endpoint
- ✅ Pydantic schemas for data validation
- ✅ Configuration management with environment variables
- ✅ Project structure following best practices
- ✅ Ready for `uv` and `ruff`

## Features

- 🚀 Zero external dependencies (pure Python standard library)
- 📦 Generates production-ready FastAPI structure
- 🎯 Simple and intuitive CLI
- 🔧 Includes configuration templates
- 📚 Well-documented generated code

## Commands

```bash
fastapi-boilerplate create <project-name>    # Create new project
fastapi-boilerplate --help                   # Show help
```
