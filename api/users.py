from typing import Optional
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()

Users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@router.get("/")
async def root():
    return {"Hello": "World"}


@router.get("/users")
async def get_users():
    return Users


@router.post("/users")
async def create_users(user: User):
    Users.append(user)
    return "Success"


@router.get("/users/{id}")
async def get_user(id: int):
    return {"user": Users[id]}
