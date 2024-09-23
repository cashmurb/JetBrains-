from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Cash"}


@app.get("/hi/{name}")
async def say_hello(name: str):
    return {"message": f"Hi {name}"}
