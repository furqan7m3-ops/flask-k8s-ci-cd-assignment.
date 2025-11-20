from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "App is running successfully!"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}
