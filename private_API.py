from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, UUID4
from typing import Optional
import secrets
import string

app = FastAPI(title='Private Client\'s Service API', version='1.0.0')

class ErrorStr(BaseModel):
    detail: str

class ID(BaseModel):
    id: UUID4
    new_pwd: Optional[str]

class Client():
    def __init__(self, id) -> None:
        self.id = id
        self.pwd = self.generate_password(10)

    def generate_password(self, length):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return password
    
    def save(self):
        pass

@app.post("/api/int/v1.0/rest/client/{id}", response_model=ID, responses={500: {"model": ErrorStr}, 501: {"model": ErrorStr}})
def create_client(id: UUID4):
    
    client = Client(id)
    try:
        client.save()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"id": id}