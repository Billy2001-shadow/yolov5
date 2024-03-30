#!/bin/bash
source ~/miniforge-pypy3/etc/profile.d/conda.sh
cd ~/yolov5/
conda activate yolov5
python detect.py --weights yolov5s.pt --source 0
