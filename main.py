import uuid

from fastapi import FastAPI

from db import create_table, add_user, update_user, delete_user, get_users
from models import User, EditUser

app = FastAPI()
create_table()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get(path="/user/all")
async def get_all_users():
    users_list = []
    users = get_users()
    for user in users:
        users_list.append(
            {
                "id": user[0],
                "fullname": user[1],
                "email": user[2],
            }
        )
    return users_list


@app.post(path="/user/new")
async def new_user(user: User):
    try:
        add_user(
            user_id=str(uuid.uuid4()),
            fullname=user.fullname,
            email=user.email
        )
    except Exception:
        return {"message": "User creation failed"}
    return {"message": "User created"}


@app.put(path="/user/edit")
async def edit_user(user: EditUser):
    try:
        update_user(
            user_id=user.user_id,
            fullname=user.fullname,
            email=user.email
        )
    except Exception:
        return {"message": "User not found"}
    return {"message": "User updated"}


@app.delete(path="/user/delete")
async def remove_user(user_id: str):
    try:
        delete_user(user_id=user_id)
    except Exception:
        return {"message": "User not found"}
    return {"message": "User deleted"}
