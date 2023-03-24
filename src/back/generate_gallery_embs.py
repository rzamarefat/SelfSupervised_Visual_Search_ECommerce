import os
from tqdm import tqdm 
from glob import glob
from Recommender import Recommender
from PIL import Image 
import numpy as np



def generate_gallery_embs(root_path_to_images, root_path_to_save):
    if not(os.path.isdir(root_path_to_save)):
        os.mkdir(root_path_to_save)


    images = [f for f in sorted(glob(root_path_to_images))]

    for img_p in tqdm(images):
        img = Image.open(img_p)
        img_name = img_p.split("/")[-1].split(".")[0]

        try:
            emb = re.gen_embs(img)
            np.save(os.path.join(root_path_to_save, f"{img_name}.npy"), emb)
        except Exception as e:
            print(e)
            continue



if __name__ == "__main__":
    root_path_to_images = rf"/media/rzamarefat/New Volume/My_Datasets/big/fashion-dataset/images/*"
    root_path_to_save = rf"/media/rzamarefat/New Volume/My_Datasets/big/fashion-dataset/simclr_embs"
    re = Recommender()
    print("KKKKKK")
    generate_gallery_embs(root_path_to_images, root_path_to_save)