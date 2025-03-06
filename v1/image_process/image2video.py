import cv2
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
import os
from subprocess import call


IMG_DIR = "/home/joshuawen/WorkSpace/MixFormer/results/vis/VisDrone-SOT-demo-2/img_res"
RES_DIR = os.path.join("/home/joshuawen/WorkSpace/MixFormer/results/vis/VisDrone-SOT-demo-2", "res_interfere_video.mp4")
FPS = 25
SIZE = (1904, 1071)

fourcc = VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter(RES_DIR, fourcc, FPS, SIZE)
img_list = sorted(os.listdir(IMG_DIR))
print(len(img_list))
for img in img_list:
    frame = cv2.imread(os.path.join(IMG_DIR, img))
    frame = cv2.resize(frame, SIZE)
    video_writer.write(frame)

video_writer.release()
