from fastapi import FastAPI, Path, HTTPException, Body, Request, Form
from fastapi.responses import HTMLResponse
import uvicorn
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")
users = []


class User(BaseModel):
    user_id: int
    username: str
    age: int


@app.get("/")
async def all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {'request': request, 'users': users})


@app.get(path="/user/{user_id}")
async def us(request: Request) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {'request': request, 'users': users})
    except IndexError:
        return HTMLResponse(status_code=404, detail="Massage not found")


@app.post("/user/{username}/{age}")
async def create(item: User) -> str:
    user_id = len(users)
    users.append({'user_id': user_id, 'username': item.username, 'age': item.age})
    return f"Информация о пользователе. Имя: {item.username}, возраст {item.age} добавлена"


@app.put("/user/{user_id}/{username}/{age}")
async def modify(user_id: int, username: str, age: int) -> str:
    try:
        modify_str = users[user_id]
        modify_str.username = username
        modify_str.age = age
        return f'Информация о пользователе {user_id} обновлена'
    except IndexError:
        raise HTTPException(status_code=404, detail=f'User {user_id} not found')


@app.delete("/user/{user_id}")
async def user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f'Пользователь {user_id} удален'
    except IndexError:
        raise HTTPException(status_code=404, detail='Massage not found')


if __name__ == "__main__":
    uvicorn.run("module_16_5:app", port=8000, log_level="info")
