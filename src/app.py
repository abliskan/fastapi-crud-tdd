from fastapi import FastAPI

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Ricky",
        last_name="Suhanry",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Erika",
        last_name="Jamali",
        gender=Gender.female,
        roles=[Role.student]
    )
]

# run: pipenv run uvicorn src.app:app | uvicorn src.app:app
@app.get("/")
async def hello():
    # app_message = os.environ.get("APP_MESSAGE", "Hello")
    return {"message": "Hello World!"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;
