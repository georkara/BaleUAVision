import glob
import os
import argparse
from natsort import natsorted
import numpy as np

# Default location-based split:
# Xanthi: 0-13
# Drama: 14-15
#
# Altitude categories:
# 50m: {1,2,3,5,6,8}
# 80m: {16}
# 100m: {4,7,9,10,11,12,13,14,15}

def split_dataset(path, train_ids, val_ids):
    folders = natsorted(os.listdir(path))
    folders = np.array(folders)

    train_folders = folders[train_ids]
    valid_folders = folders[val_ids]

    with open('train.txt', 'w') as f:
        for folder in train_folders:
            imgs = glob.glob(os.path.join(path, folder, 'images', '*.JPG'))
            for img in imgs:
                f.write(f"{img}\n")

    with open('valid.txt', 'w') as f:
        for folder in valid_folders:
            imgs = glob.glob(os.path.join(path, folder, 'images', '*.JPG'))
            for img in imgs:
                f.write(f"{img}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split dataset into train and validation sets by folder indices.")

    parser.add_argument('--path', type=str, default='data', help='Path to the main data directory (default: bales/data).')
    parser.add_argument('--train_ids', type=int, nargs='+', help='Indices of folders for training set.')
    parser.add_argument('--val_ids', type=int, nargs='+', help='Indices of folders for validation set.')

    args = parser.parse_args()

    if args.train_ids is None or args.val_ids is None:
        # Default scenario split by location (Xanthi: 0-13, Drama: 14-15)
        default_train_ids = list(range(0, 14))  # Xanthi (0-13)
        default_val_ids = [14, 15]  # Drama (14-15)
        split_dataset(args.path, default_train_ids, default_val_ids)
    else:
        split_dataset(args.path, args.train_ids, args.val_ids)