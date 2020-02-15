import wandb

# At the top of your script
config = dict (
  learning_rate = 0.01,
  momentum = 0.2,
  architecture = "CNN",
  dataset_id = "peds-0192",
  infra = "AWS",
)

wandb.init(
  project="detect-pedestrians",
  notes="tweak baseline",
  tags=["baseline", "paper1"],
  config=config,
)

# Inside your training loop
acc = 0.78
loss = 0.21
ped_acc = 0.62
car_acc = 0.92
tree_acc = 0.81

wandb.log({
  "accuracy": acc,
  "loss": loss,
  "class_acc": {
    "pedestrian": ped_acc,
    "car": car_acc,
    "tree": tree_acc,
  }
})

