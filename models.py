from pydantic import BaseModel


class User(BaseModel):

    fullname: str
    email: str


class EditUser(User):
    user_id: str
