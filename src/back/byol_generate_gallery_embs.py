import torch
from torchvision import transforms as T
from another_byol import BYOL
from torchvision import models
import cv2
import random
from glob import glob
from PIL import Image
from tqdm import tqdm
import numpy as np
from sklearn.neighbors import NearestNeighbors
from config import PATH_TO_PRETRAINED_WEIGHTS_BYOL
import os

model = models.resnet18(pretrained=False)
model = BYOL(model, in_features=512, batch_norm_mlp=True)

device = 'cuda'


test_transform = T.Compose([
                T.Resize((256, 256)),
                T.ToTensor(),
                T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]) ])


try: 
    model = model.to(device)
    model.load_state_dict(torch.load(PATH_TO_PRETRAINED_WEIGHTS_BYOL))
    model.eval()
    print("=====> Pretrained weights loaded successfully")
except Exception as e:
    print("=====> Sth went wrong in loading pretrained weights SimCLR")
    print(e)


def generate_gallery_embs(root_path_to_images, root_path_to_save):
    if not(os.path.isdir(root_path_to_save)):
        os.mkdir(root_path_to_save)


    images = [f for f in sorted(glob(root_path_to_images))]

    for img_p in tqdm(images):
        try:
            img = Image.open(img_p)
            img = test_transform(img)
            img = torch.unsqueeze(img, dim=0)
            img = img.to(device)
            emb = model(img)
            emb = emb.detach().to(device).numpy()
            np.save(os.path.join(root_path_to_save, img_p.split('/')[-1].replace('jpg', 'npy')), emb)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    images = [f for f in  sorted(glob("/home/rmarefat/projects/github/recommender/resized/*"))]
    

    

    
