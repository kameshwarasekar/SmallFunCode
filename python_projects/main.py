from fastapi import FastAPI
import pandas as ps

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
