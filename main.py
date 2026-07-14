from fastapi import FastAPI

app = FastAPI(title="CloudMind Test App")


@app.get("/")
def root():
    return {
        "message": "Hello from CloudMind test app",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
