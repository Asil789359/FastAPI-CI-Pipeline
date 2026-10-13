from fastapi import FastAPI

app = FastAPI(
    title="DevOps Demo API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "FastAPI CI/CD Pipeline",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/add")
def add(a: int, b: int):
    return {
        "result": a + b
    }
