import os
from tqdm import tqdm 
from glob import glob
from Recommender import Recommender
from PIL import Image 
import numpy as np
import torch
import torchvision
import lightly
from SimCLR import SimCLRModel
from config import PATH_TO_PRETRAINED_WEIGHTS_SIMCLR
from sklearn.preprocessing import normalize


try:
    simclr = SimCLRModel()
    path_to_weights = PATH_TO_PRETRAINED_WEIGHTS_SIMCLR
    ckpt = torch.load(path_to_weights, map_location=torch.device('cpu'))
    simclr.load_state_dict(ckpt['state_dict'])
    simclr.eval()
    simclr.to(device)
    print("=====> Pretrained weights loaded successfully")
except Exception as e:
    print("=====> Sth went wrong in loading pretrained weights SimCLR")
    print(e)

test_transforms = torchvision.transforms.Compose([
        torchvision.transforms.Resize((input_size, input_size)),
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Normalize(
            mean=lightly.data.collate.imagenet_normalize['mean'],
            std=lightly.data.collate.imagenet_normalize['std'],
        )
    ])



def gen_embs(image):
        image = test_transforms(image)
        image = torch.unsqueeze(image, dim=0)

        image = image.to(device)
        
        emb = simclr.backbone(image).flatten(start_dim=1)
        
        emb = emb.to('cpu').detach().numpy()
        emb = normalize(emb)

        return emb


def generate_gallery_embs(root_path_to_images, root_path_to_save):
    if not(os.path.isdir(root_path_to_save)):
        os.mkdir(root_path_to_save)


    images = [f for f in sorted(glob(root_path_to_images))]

    for img_p in tqdm(images):
        img = Image.open(img_p)
        img_name = img_p.split("/")[-1].split(".")[0]

        try:
            emb = gen_embs(img)
            np.save(os.path.join(root_path_to_save, f"{img_name}.npy"), emb)
        except Exception as e:
            print(e)
            continue



if __name__ == "__main__":
    root_path_to_images = rf"/media/rzamarefat/New Volume/My_Datasets/big/fashion-dataset/images/*"
    root_path_to_save = rf"/media/rzamarefat/New Volume/My_Datasets/big/fashion-dataset/simclr_embs"

    input_size = 128
    device = 'cpu'
    generate_gallery_embs(root_path_to_images, root_path_to_save)