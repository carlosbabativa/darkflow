# Prepare dataset for training
# splits images and annotations into respective folders
# from  {dataset_folder}/data_train containing the full collection of images and annotations

import sys
import argparse
import os
from os.path import join as join_pth
from shutil import copytree as cp, ignore_patterns

ds_name = None
parser = argparse.ArgumentParser()
parser.add_argument(
    '-d',
    '--dataset',
    dest='ds_name',
    required=True,
    help='Name of dataset (folder in datastes folder \'data\')',
)
args = parser.parse_args()
def main(args):
	ds_name = args.ds_name
	ds_path = join_pth('data', ds_name)
	dt_path = join_pth(ds_path,'data_train')
	ds_img_pth = join_pth(ds_path,'images')
	ds_ans_pth = join_pth(ds_path,'annots')

	cp(dt_path, ds_img_pth, ignore=ignore_patterns('*.xml'))
	cp(dt_path, ds_ans_pth, ignore=ignore_patterns('*.jpg'))


if __name__=="__main__":
    main(args)
