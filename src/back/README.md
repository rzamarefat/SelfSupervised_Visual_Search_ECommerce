### Instruction


#### Running Server
- make a virtual environment
```
python3 -m venv ./venv
```
- Activate the env:
```
source ./venv/bin/activate
```
- Run the server:
```
uvicorn main:app --reload
```



#### Generating gallery embeddings
- download SimCLR and BYOL checkpoints from the following links
```
https://drive.google.com/file/d/1ijKA-5wkjFHazVfCG_N-qlWCu2f_gR9u/view?usp=share_link
https://drive.google.com/file/d/1oBVszRlby7GBVpqxCog9n7dGr2Ej31Ao/view?usp=share_link
```
- use the following modules for generating embeddings
```
simclr_generate_gallery_embs.py
byol_generate_gallery_embs.py
```