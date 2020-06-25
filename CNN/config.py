import os

# initialize the path to the original input directory of images
orig_input_dataset = "/home/aalarie/DancerNet/Images"

# initialize the base path to the new directory that will contain
# our images after computing the training and testing split
base_path = "/home/aalarie/DancerNet/Images"

# derive the training, validation, and testing directories
train_path = os.path.sep.join([base_path, "training"])
val_path = os.path.sep.join([base_path, "validation"])
test_path = os.path.sep.join([base_path, "testing"])

# define the amount of data that will be used training
train_split = 0.8

# the amount of validation data will be a percentage of the
# training data
val_split = 0.1