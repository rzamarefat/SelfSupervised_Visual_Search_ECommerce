from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import base64
import random
from glob import glob
from fastapi import Body
from fastapi import FastAPI

from Recommender import Recommender
import os


rec = Recommender()

class Item(BaseModel):
    id: str
    embApproach: str
    

def get_random_images():
    data = []
    random_images = random.sample([f for f in sorted(glob("/media/rzamarefat/New Volume/My_Datasets/big/fashion-dataset/images/*"))], 12)

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
    
    return {"images": data}


@app.post("/item")
def item(request: Item):
    print("====>", request.json().split(" "))

    id = request.json().split(" ")[1].replace('"', "").replace('"', "").replace(",", "")
    emb_approach = request.json().split(" ")[-1].replace('"', "").replace('"', "").replace("}", "")

    final_recoms = rec.recommend(id, emb_approach, k=20)
    


    if os.path.isfile("./RECOMS.txt"):
        os.remove("./RECOMS.txt")

    with open("./RECOMS.txt", "a+") as h:
        h.seek(0)
        h.writelines(f"EMB_APPROACH: {emb_approach} \n")
        
        for f in final_recoms:
            h.seek(0)
            h.writelines(f + "\n")
    print("===========done wrinting recoms")

    
    return None

@app.get("/item")
def item():
    print("reading recoms")
    with open("./RECOMS.txt", "r") as h:
        data = [l for l in h.readlines()]

    emb_approach = [l.replace("\n", "") for l in data if l.__contains__("EMB_APPROACH")][0].split(" ")[1]

    recoms = [l.replace("\n", "") for l in data if not(l.__contains__("EMB_APPROACH"))]
    

    data = []
    for r in recoms:
        with open(r, "rb") as image_file:
            data.append({
                "id":r.split("/")[-1].split(".")[0],
                "image": base64.b64encode(image_file.read())
                })
    
    return {"images": data}




