from fastapi import FastAPI, Path
import uvicorn

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def us() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create(username: str = Path(min_length=5, max_length=20, description='Enter username'),
                 age: int = Path(ge=15, le=120, description='Enter age')) -> str:
    current_index = str(len(users) + 1)
    users[current_index] = f'Имя: {username} Возраст: {age}'
    return f"Пользователь {current_index} добавлен. Имя: {username}, Возраст: {age}"


@app.put("/user/{user_id}/{username}/{age}")
async def modify(user_id: int = Path(ge=1, le=100, description='Enter User ID'),
                 username: str = Path(min_length=5, max_length=20, description='Enter username'),
                 age: int = Path(ge=15, le=120, description='Enter age')) -> str:
    users[user_id] = f'Имя: {username} Возраст: {age}'
    return f"Пользователь № {user_id} изменен. Имя: {username}, Возраст: {age}"


@app.delete("/user/{user_id}")
async def user(user_id: int = Path(ge=1, le=100, description='Enter User ID')) -> str:
    users.pop(str(user_id))
    return f'Пользователь № {user_id} удален'


if __name__ == "__main__":
    uvicorn.run("module_16_3:app", port=8000, log_level="info")
