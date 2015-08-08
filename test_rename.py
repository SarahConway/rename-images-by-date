from rename_photos_by_date import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", dest="opt_str", action="store")
parser.add_argument("-p", dest="path", action="store")
args = parser.parse_args()

batch_img_rename_by_date(args.path, args.opt_str)
