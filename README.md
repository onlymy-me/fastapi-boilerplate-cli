Here is a polished, professional `README.md` optimized for your GitHub repository and PyPI description. I have structured it to highlight the "Zero Dependency" feature and fully embraced `uv` as the primary workflow tool as requested.

````markdown
# FastAPI Boilerplate CLI

<div align="center">

![FastAPI Boilerplate CLI](https://img.shields.io/pypi/v/fastapi-boilerplate-cli?color=blue&style=for-the-badge)
![Python Versions](https://img.shields.io/pypi/pyversions/fastapi-boilerplate-cli?style=for-the-badge)
![License](https://img.shields.io/pypi/l/fastapi-boilerplate-cli?style=for-the-badge)

**⚡ Kickstart production-ready FastAPI projects in seconds.**

[View on PyPI](https://pypi.org/project/fastapi-boilerplate-cli/) • [View on GitHub](https://github.com/onlymy-me/fastapi-boilerplate-cli)

</div>

---

## 📖 About

**FastAPI Boilerplate CLI** is a lightweight command-line tool designed to generate a robust FastAPI directory structure with best practices built-in.

Unlike other generators that require heavy dependencies, this tool is **pure Python** with **zero external dependencies**, making it instant to install and run. It scaffolds projects pre-configured for modern Python tooling like `uv` and `ruff`.

## ✨ Features

- **🚀 Zero Dependencies:** The CLI itself relies only on the Python standard library.
- **⚡ Built for `uv`:** First-class support for the `uv` package manager.
- **🏗️ Modular Architecture:** Generates a router-based structure (`app/routers`, `app/schemas`).
- **🛡️ Type Safety:** Includes Pydantic models for request/response validation.
- **⚙️ Config Management:** Built-in `pydantic-settings` for `.env` management.
- **✅ Code Quality:** Pre-configured `pyproject.toml` with `ruff` for linting and formatting.

## 📦 Installation

Since this tool is built for the modern Python ecosystem, we recommend installing it globally using `uv`.

```bash
uv tool install fastapi-boilerplate-cli
````

*Alternatively, using pip:*

```bash
pip install fastapi-boilerplate-cli
```

## 🚀 Usage

### 1\. Create a Project

Generate a new project scaffold in seconds:

```bash
fastapi-boilerplate create my-awesome-api
```

### 2\. Install Dependencies

Navigate to your new project and sync dependencies using `uv`:

```bash
cd my-awesome-api

# Install dependencies using uv
uv pip install -r requirements.txt
```

### 3\. Run the Server

Start the development server with hot-reloading:

```bash
uvicorn main:app --reload
```

Visit `http://localhost:8000/docs` to see your interactive API documentation\!

## 📂 What Gets Generated?

The tool creates a clean, scalable structure:

```text
my-awesome-api/
├── app/
│   ├── routers/          # API route handlers (endpoints)
│   ├── schemas/          # Pydantic models (data validation)
│   ├── config.py         # Environment configuration
│   ├── dependencies.py   # Dependency injection (DB, Auth)
│   └── __init__.py
├── main.py               # Application entry point
├── pyproject.toml        # Project metadata & Ruff config
├── requirements.txt      # Project dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Standard Python gitignore
└── README.md             # Project documentation
```

## 🛠 Tech Stack

The generated boilerplate includes specific, compatible versions of:

  * **FastAPI**
  * **Uvicorn** (Standard)
  * **Pydantic** (v2+)
  * **Pydantic Settings**

## 🤝 Contributing

This project is new and open to improvements\! If you find a bug or have a feature request (like Docker support or specific DB integrations), please open an issue or submit a PR.

1.  Fork the repository
2.  Create your feature branch (`git checkout -b feature/amazing-feature`)
3.  Commit your changes (`git commit -m 'Add some amazing feature'`)
4.  Push to the branch (`git push origin feature/amazing-feature`)
5.  Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

```
```
