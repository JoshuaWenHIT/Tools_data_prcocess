import subprocess as sp

list_path = '/media/joshuawen/Data/video_det/video_test/video_makeup/list.txt'
concat_name = '/media/joshuawen/Data/video_det/video_test/video_makeup/concat.mp4'

command = [
    'ffmpeg',
    '-f', 'concat',
    '-safe', '0',
    '-i', list_path,
    '-c', 'copy',
    concat_name
]

p = sp.call(command)
