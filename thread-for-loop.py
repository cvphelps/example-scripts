# Example: multiple runs in one thread
# This script calls wandb.init in a for loop to create 10 runs.
# reinit=True works to let you call wandb.init multiple times in
# the same script.

import wandb

for x in range(10):
	wandb.init(project="for-loop-runs", reinit=True)
	for y in range (100):
		wandb.log({"metric": x+y})
	

