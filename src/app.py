# src/app.py
from .utils import logger
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # create a new API

logger.log("DEBUG", "Starting the server")

##
## Data Models
##

# a user on the platform
class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    password: str
    status: str
    created_on: str
    last_logged_in_on: str

# a token, such as a verification token or a refresh token
class Token(BaseModel):
    id: int
    user_id: int
    token_type: str
    token: str
    expires_on: str

# verify a user registration input
class VerifyRegisterInput(BaseModel):
    email: str
    verification_code: str

# the input to refresh an access_token
class RefreshTokenInput(BaseModel):
    access_token: str
    refresh_token: str

# create a quick test user for validation as a placeholder
user: User = User(
    id=1,
    first_name="Kevin",
    last_name="Eaton",
    email="kevinhowardeaton@gmail.com",
    password="",
    status="active",
    created_on="2023-06-02T00:00:00Z",
    last_logged_in_on="2023-06-02T00:00:00Z"
)

##
## Routes
##

# health check
@app.get("/")
async def health_route():
    return {"status": "up"}

# register
@app.post("/users")
async def register_route(user: User) -> User:
    return user

# verify registration
@app.post("/users/verify")
async def user_verify_route(input: VerifyRegisterInput) -> User:
    return user

# login
@app.post("/login")
async def login_route(user: User) -> User:
    return user

# get the logged-in user's profile
@app.get("/me")
async def get_profile_route() -> User:
    return user

# update the logged-in user's profile
@app.patch("/me")
async def update_profile_route(user: User) -> User:
    return user

## refresh a token
@app.post("/me/refresh")
async def refresh_token_route(input: RefreshTokenInput) -> RefreshTokenInput:
    return {"route": "refresh_token_route"}

## get a user by id
@app.get("/users/{id}")
async def get_user_profile_route(id: int) -> User:
    return user