import torch
from SimCLR import SimCLRModel
import torchvision
import cv2
from PIL import Image
import lightly
from sklearn.preprocessing import normalize
import faiss
import numpy as np
import faiss
from glob import glob

class Recommender():
    def __init__(self):
        self.device = 'cpu'
        self.path_to_embs = "/media/rzamarefat/New Volume/My_Datasets/big/fashion-dataset/simclr_embs/*"

        try:
            self._simclr = SimCLRModel()
            self.path_to_weights = "/home/rzamarefat/projects/github_projects/Recom/SimCLR_Visual_Search_React/src/back/epoch=19-step=2960.ckpt"
            self.ckpt = torch.load(self.path_to_weights, map_location=torch.device('cpu'))
            self._simclr.load_state_dict(self.ckpt['state_dict'])
            self._simclr.eval()
            self._simclr.to(self.device)
            print("=====> Pretrained weights loaded successfully")
        except Exception as e:
            print("=====> Sth went wrong in loading pretrained weights")
            print(e)
        
        self._embs_dim = 512
        

        self._build_faiss()
        

        self._input_size = 128
        

        self.test_transforms = torchvision.transforms.Compose([
                        torchvision.transforms.Resize((self._input_size, self._input_size)),
                        torchvision.transforms.ToTensor(),
                        torchvision.transforms.Normalize(
                            mean=lightly.data.collate.imagenet_normalize['mean'],
                            std=lightly.data.collate.imagenet_normalize['std'],
                        )
        ])

    def _build_faiss(self):

        self._faiss_index = faiss.IndexFlatIP(self._embs_dim)

        embs = [(self._read_npy(f), f.split("/")[-1].split(".")[0]) for f in sorted(glob(self.path_to_embs))]

        
        self.map_required_for_faiss_fetch = {}
        for index, (emb_f, emb_name) in enumerate(embs):
            self._faiss_index.add(emb_f)
            self.map_required_for_faiss_fetch[index] = emb_name

    def gen_embs(self, image):
        image = self.test_transforms(image)
        image = torch.unsqueeze(image, dim=0)

        image = image.to(self.device)
        emb = self._simclr.backbone(image).flatten(start_dim=1)
        emb = emb.to('cpu').detach().numpy()
        emb = normalize(emb)

        return emb
    
    def _read_npy(self, abs_path):
        with open(abs_path, "rb") as handle:
            data = np.load(handle, allow_pickle=True)
        
        return data


    def recommend(self, query_image, k=10):
        query_emb = self.gen_embs(query_image)
        distance, id_ = self._faiss_index.search(query_emb, k)


        print(distance, id_)
        for i in id_[0]:
            print(self.map_required_for_faiss_fetch[i])



if __name__ == "__main__":
    r = Recommender()
    path_to_image = "/home/rzamarefat/projects/github_projects/Recom/SimCLR_Visual_Search_React/src/back/10023.jpg"
    img = Image.open(path_to_image)
    r.recommend(img)