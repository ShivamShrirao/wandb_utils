from tqdm import tqdm
from sys import argv
import wandb

api = wandb.Api()

runs = api.runs("shivamshrirao/"+argv[1])

for run in tqdm(runs):
    if run.id != "3vhz3cie":
        print(run)
        run.config["dropout_type"] = "Dropout"
        run.update()