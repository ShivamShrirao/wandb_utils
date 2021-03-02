import wandb
from sys import argv

api = wandb.Api()

runs = api.runs("shivamshrirao/"+argv[1])

for run in runs:
    history = run.history()
    run.summary['best_val_dsc'] = history['val_dsc'].max()
    print(run.name, run.summary['best_val_dsc'])
    run.update()