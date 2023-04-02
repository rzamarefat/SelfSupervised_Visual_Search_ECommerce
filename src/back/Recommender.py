from PIL import Image

import faiss
import numpy as np
import faiss
from glob import glob
from tqdm import tqdm
import os
import torchvision
import lightly
from config import PATH_TO_EMBS_SIMCLR,PATH_TO_EMBS_BYOL, PATH_TO_IMAGES
import torchvision
from BYOL import BYOL


class Recommender():
    def __init__(self):
        self.device = 'cpu'
        self.path_to_embs_simclr = PATH_TO_EMBS_SIMCLR
        self.path_to_embs_byol = PATH_TO_EMBS_BYOL
        self.path_to_images = PATH_TO_IMAGES
        self._limit_for_gallery = 16000

        try:
            torchvision.models.resnet18(pretrained=False)
            model = BYOL(model, in_features=512, batch_norm_mlp=True)
        except Exception as e:
            print("=====> Sth went wrong in loading pretrained weights BYOL")
            print(e)
        
        self._embs_dim = 512
        

        self._build_faiss()
        print("======> Done with the FAISS!")
        
        
        

    def _build_faiss(self):
        print("=====> Applications is making the FAISS part.")
        self._faiss_index_simclr = faiss.IndexFlatIP(self._embs_dim)
        self._faiss_index_byol = faiss.IndexFlatIP(self._embs_dim)

        embs_simclr = [(f, f.split("/")[-1].split(".")[0]) for f in sorted(glob(os.path.join(self.path_to_embs_simclr, "*")))]
        print("=====> Number of images in database", len(embs_simclr))

        
        self.map_required_for_faiss_fetch_simclr = {}
        for index, (emb_f, emb_name) in tqdm(enumerate(embs_simclr), total=len(embs_simclr)):
            if index >= self._limit_for_gallery:
                break
            emb_f = self._read_npy(emb_f)
            self._faiss_index_simclr.add(emb_f)
            self.map_required_for_faiss_fetch_simclr[index] = emb_name


        embs_byol = [(f, f.split("/")[-1].split(".")[0]) for f in sorted(glob(os.path.join(self.path_to_embs_byol, "*")))]
        self.map_required_for_faiss_fetch_byol = {}
        for index, (emb_f, emb_name) in tqdm(enumerate(embs_byol), total=len(embs_byol)):
            if index >= self._limit_for_gallery:
                break
            emb_f = self._read_npy(emb_f)
            self._faiss_index_byol.add(emb_f)
            self.map_required_for_faiss_fetch_byol[index] = emb_name
    
    def _read_npy(self, abs_path):
        with open(abs_path, "rb") as handle:
            data = np.load(handle, allow_pickle=True)
        
        return data


    def recommend(self, query_image_id, emb_approach="SIMCLR", k=10):
        final_recoms = []

        if emb_approach == "SIMCLR":
            print("======> ", "using simclr embs")
            query_emb = self._read_npy(os.path.join(self.path_to_embs_simclr, f"{query_image_id}.npy"))
            distance, id_ = self._faiss_index_simclr.search(query_emb, k)    
            for i in id_[0]:
                final_recoms.append(os.path.join(self.path_to_images, f"{self.map_required_for_faiss_fetch_simclr[i]}.jpg"))

        elif emb_approach == "BYOL":
            print("======> ", "using byol embs")
            query_emb = self._read_npy(os.path.join(self.path_to_embs_byol, f"{query_image_id}.npy"))
            distance, id_ = self._faiss_index_byol.search(query_emb, k)
            for i in id_[0]:
                final_recoms.append(os.path.join(self.path_to_images, f"{self.map_required_for_faiss_fetch_byol[i]}.jpg"))
        else:
            raise NotImplementedError("Please provide a valid emb generator (options: SIMCLR/BYOL)")

        return final_recoms



if __name__ == "__main__":
    r = Recommender()
    path_to_image = "/home/rzamarefat/projects/github_projects/Recom/SimCLR_Visual_Search_React/src/back/2115.jpg"
    img = Image.open(path_to_image)
    # r.recommend(img)
    r.gen_embs(img)

    print()