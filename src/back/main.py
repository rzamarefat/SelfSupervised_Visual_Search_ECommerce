from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import cv2
import io
from starlette.responses import StreamingResponse
import base64

data = []
with open("/media/rzamarefat/New Volume/My_Datasets/big/fashion-dataset/2115.jpg", "rb") as image_file:
    img_1 = base64.b64encode(image_file.read())

with open("/media/rzamarefat/New Volume/My_Datasets/big/fashion-dataset/9083.jpg", "rb") as image_file:
    img_2 = base64.b64encode(image_file.read())
with open("/media/rzamarefat/New Volume/My_Datasets/big/fashion-dataset/10023.jpg", "rb") as image_file:
    img_3 = base64.b64encode(image_file.read())

data.append(img_1)
data.append(img_2)
data.append(img_3)


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
    # res, im_png = cv2.imencode(".png", image)
    # return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")
    return {"images": [img_1, img_2]}