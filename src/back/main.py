from fastapi import FastAPI, Body, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import cv2
import io
from starlette.responses import StreamingResponse
import base64
import random
from glob import glob
from fastapi import Body
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder

class Item(BaseModel):
    id: str
    

def get_random_images():
    data = []
    random_images = random.sample([f for f in sorted(glob("/media/rzamarefat/New Volume/My_Datasets/big/fashion-dataset/images/*"))], 20)

    for ri in random_images:
        with open(ri, "rb") as image_file:
            data.append({
                "id":ri.split("/")[-1].split(".")[0],
                "image": base64.b64encode(image_file.read())
                })

    return data

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Root page"}


@app.get("/explore")
def root():
    data = get_random_images()
    return {"images": data}


@app.post("/item")
async def item(request: Item):
    
    return request.json()