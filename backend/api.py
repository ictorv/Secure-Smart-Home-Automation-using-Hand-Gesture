from fastapi import FastAPI, HTTPException,File,UploadFile
from pydantic import BaseModel
import database


app = FastAPI()

# Define Pydantic models
class User(BaseModel):
    email: str
    username: str
    password: str
    photo: UploadFile

# Define FastAPI endpoints
@app.post("/user/")
async def create_user(user: User):
    image = user.photo
    # Process the image file as needed
    filename = image.filename
    content = await image.read()
    with open(filename, "wb") as file:
        file.write(content)
    database.insertBLOB(user.email, user.username, user.password, user.photo)
    return {"filename": filename}

@app.get("/user/{username}")
def read_user(username: str):
    return database.retrieveUserDetails(username)
