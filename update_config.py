from tqdm import tqdm
import wandb

api = wandb.Api()

runs = api.runs("shivamshrirao/3d_attn_aug_res_unet")

for run in tqdm(runs):
    if run.id != "3vhz3cie":
        print(run)
        run.config["dropout_type"] = "Dropout"
        run.update()