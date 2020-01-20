import wandb

for x in range(10):
	wandb.init(project="for-loop-runs", reinit=True)
	for y in range (100):
		wandb.log({"metric": x+y})
	

