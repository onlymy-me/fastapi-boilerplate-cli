from fastapi import FastAPI
from app.routers import health

app = FastAPI(
    title="ui",
    description="A FastAPI boilerplate project",
    version="0.1.0"
)

# Include routers
app.include_router(health.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to ui"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
