from fastapi import FastAPI

app = FastAPI(
    title="SyncMeet API",
    description="Real-time collaboration backend",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "SyncMeet backend is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }