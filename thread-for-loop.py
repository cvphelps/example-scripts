import wandb
import random

hyperparameter_defaults = dict(
	dropout = 0.5,
	batch_size = 100,
	learning_rate = 0.001,
	epochs = 2,
	)

for x in range(10):
	wandb.init(config=hyperparameter_defaults, project="for-loop-runs", reinit=True)
	for y in range (100):
		wandb.log({"metric": random.random()+x+y})
	

