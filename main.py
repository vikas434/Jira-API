from fastapi import FastAPI

app = FastAPI()

@app.get("/", summary="Root Endpoint", description="Returns a simple Hello World message.")
async def read_root():
    """
    This endpoint returns a simple JSON object with a greeting message.
    """
    return {"message": "Hello, World!"} 