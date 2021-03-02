from tqdm import tqdm
from sys import argv
import wandb

api = wandb.Api()

runs = api.runs("shivamshrirao/"+argv[1])

ftype = "media/images/Outputs"

for run in tqdm(runs):
    fnames = []
    for x in run.files(per_page=1000):
        if ftype in x.name:
            fnames.append(x.name)
    fnames.sort(key=lambda x: int(x.split('_')[1]))
    for fn in fnames[:-1]:
        file = run.file(fn)
        print(file)
        file.delete()
