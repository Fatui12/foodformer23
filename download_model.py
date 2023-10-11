import wandb
import os
from pathlib import Path
# wandb_team = 'mlops-usf'
# wandb_proj = 'foodformer'
# wandb_loc  = 

wandb.init()
path = wandb.use_artifact('rileyhu7481/Foodformer/model-lvv772mv:v0').download(root='./serving')