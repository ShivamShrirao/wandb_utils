import wandb

api = wandb.Api()

runs = api.runs("shivamshrirao/3d_attn_aug_res_unet")

for run in runs:
    history = run.history()
    run.summary['best_val_dsc'] = history['val_dsc'].max()
    print(run.name, run.summary['best_val_dsc'])
    run.update()