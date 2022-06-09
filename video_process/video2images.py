import subprocess as sp
import os

input_video_path = '/media/ubuntu/SSD/JoshuaWen/Projects/CenterTrack/results/default_mot_mini.mp4'
fps = '25'
out_images_path = '/media/ubuntu/SSD/JoshuaWen/Projects/CenterTrack/results/default_mot_mini'

if os.path.exists(out_images_path):
    out_images_path = out_images_path + '/%06d.jpg'
else:
    os.mkdir(out_images_path)
    out_images_path = out_images_path + '/%06d.jpg'

command = [
    'ffmpeg',
    '-i', input_video_path,
    '-r', fps,
    '-f', 'image2',
    out_images_path
]

p = sp.call(command)
