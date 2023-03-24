from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import cv2
import io
from starlette.responses import StreamingResponse
import base64
import random
from glob import glob


def get_random_images():
    data = []
    random_images = random.sample([f for f in sorted(glob("/media/rzamarefat/New Volume/My_Datasets/big/fashion-dataset/images/*"))], 20)

    for ri in random_images:
        with open(ri, "rb") as image_file:
            data.append(base64.b64encode(image_file.read()))
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