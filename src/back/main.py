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
from Recommender import Recommender
import os


rec = Recommender()

class Item(BaseModel):
    id: str
    

def get_random_images():
    data = []
    random_images = random.sample([f for f in sorted(glob("/media/rzamarefat/New Volume/My_Datasets/big/fashion-dataset/images/*"))], 2)

    for ri in random_images:
        print("ri", ri)
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
    print("inside root")
    print("type(data)", type(data))
    return {"images": data}


@app.post("/item")
def item(request: Item):
    id = request.json().split(":")[1].strip().replace('"', '').replace('"', '').replace('}', '')

    final_recoms = rec.recommend(id, k=2)
    


    if os.path.isfile("./RECOMS.txt"):
        os.remove("./RECOMS.txt")

    with open("./RECOMS.txt", "a+") as h:
        for f in final_recoms:
            h.seek(0)
            h.writelines(f + "\n")
    print("===========done wrinting recoms")

    
    return None

@app.get("/item")
def item():
    print("reading recoms")
    with open("./RECOMS.txt", "r") as h:
        recoms = [l.replace("\n", "") for l in h.readlines()]
    
    data = []
    for r in recoms:
        with open(r, "rb") as image_file:
            data.append({
                "id":r.split("/")[-1].split(".")[0],
                "image": base64.b64encode(image_file.read())
                })
            
    return {"images": data}




