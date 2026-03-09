import uuid
from hashlib import md5
from fastapi import FastAPI

app = FastAPI()

@app.get("/generate/uuid4")
def gen_uuid():
    return {"result": str(uuid.uuid4())}

@app.get("/hash/md5")
def get_md5(data: str):
    hashed = md5(data.encode())
    return {"result": hashed.hexdigest()}

@app.get("/add")
def add(left: int, right: int):
    return {"result": left + right }
