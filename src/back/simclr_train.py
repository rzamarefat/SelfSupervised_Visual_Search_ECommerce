import torch
import torch.nn as nn
import pytorch_lightning as pl
import lightly
from SimCLR import SimCLRModel

num_workers = 8
batch_size = 300
seed = 1
max_epochs = 20
input_size = 128
num_ftrs = 32


pl.seed_everything(seed)


path_to_data = '/home/rmarefat/projects/github/recommender/resized'


collate_fn = lightly.data.SimCLRCollateFunction(
    input_size=input_size,
    vf_prob=0.5,
    rr_prob=0.5
)


dataset_train_simclr = lightly.data.LightlyDataset(
    input_dir=path_to_data
)


dataloader_train_simclr = torch.utils.data.DataLoader(
    dataset_train_simclr,
    batch_size=batch_size,
    shuffle=True,
    collate_fn=collate_fn,
    drop_last=True,
    num_workers=num_workers
)



if __name__ == "__main__":
    gpus = 1 if torch.cuda.is_available() else 0

    model = SimCLRModel()
    trainer = pl.Trainer(max_epochs=max_epochs, devices=gpus)
    trainer.fit(model, dataloader_train_simclr)