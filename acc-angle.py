import wandb
import random

wandb.init(project="angle-acc")

for x in range(1, 10):
	for y in range(0,360):
		wandb.log({"accuracy": x*3*y + random.random(), "angle": y})
