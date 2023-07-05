from fastapi import FastAPI

app = FastAPI()


# run: pipenv run uvicorn src.main:app | uvicorn src.app:app
@app.get("/")
def hello():
    # app_message = os.environ.get("APP_MESSAGE", "Hello")
    return {"message": "Hello World!"}

