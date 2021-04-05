import argparse, os, subprocess, sys
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument('--build', '-b', help='Docker Build', action='store_true')
parser.add_argument('--workdir', '-w', help='Working Directory to save created Git Repo or List Export', type=str, default=os.getcwd())

args = parser.parse_args()


# CON=$(docker ps -aqf "ancestor=${DIR}")
# PORT=4000

# if args.reconfig: