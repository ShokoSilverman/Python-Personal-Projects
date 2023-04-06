from fastapi import FastAPI
import pyotp

app = FastAPI()


@app.get("/")
async def read_root():
    return pyotp.random_base32()
