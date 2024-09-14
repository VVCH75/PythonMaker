from fastapi import FastAPI
import uvicorn

async def app(scope, receive, send):
    pass
app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": f"Главная страница"}

@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def welcome(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}




if __name__ == "__main__":
    uvicorn.run("module_16_1:app", port=8000, log_level="info")
