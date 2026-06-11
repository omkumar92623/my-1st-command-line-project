import argparse
import os

parser = argparse.ArgumentParser(description="file size detector")
parser.add_argument("file_name",help="enter your file name")
args =parser.parse_args()
size=os.path.getsize(args.file_name)

print(size)