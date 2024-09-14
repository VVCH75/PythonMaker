from fastapi import FastAPI, Path
import uvicorn
from typing import Annotated

async def app(scope, receive, send):
    pass
app = FastAPI()

@app.get("/user/{user_id}")
async def user(user_id: int=Path(min_length=1, max_length=100, description='Enter User ID')) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
async def welcome(username: Annotated[str,Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                  age: int=Path(ge=18, le=120, description='Enter age', example=24)) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

if __name__ == "__main__":
    uvicorn.run("module_16_2:app", port=8000, log_level="info")
