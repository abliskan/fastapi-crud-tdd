from fastapi import FastAPI

app = FastAPI()

# run: pipenv run uvicorn src.main:app
@app.get("/")
def hello():
    return {"message": "Hello World!"}

