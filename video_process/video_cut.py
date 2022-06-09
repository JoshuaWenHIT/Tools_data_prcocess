import subprocess as sp
import os

input_video_path = '/media/joshuawen/Data/video_det/AnHui/output/Ued_2021_06_27_20_43_41_0000000000000000800a687c8a5920c9.mp4'

start_time = '1:21:40'
end_time = '1:25:20'

start_h = int(start_time.split(':')[0])
start_m = int(start_time.split(':')[1])
start_s = int(start_time.split(':')[2])

end_h = int(end_time.split(':')[0])
end_m = int(end_time.split(':')[1])
end_s = int(end_time.split(':')[2])

tot_diff_s = (end_h * 60 * 60 + end_m * 60 + end_s) - (start_h * 60 * 60 + start_m * 60 + start_s)

diff_h = int(tot_diff_s / 60 / 60)
diff_m = int((tot_diff_s - diff_h * 60 * 60) / 60)
diff_s = tot_diff_s - diff_h * 60 * 60 - diff_m * 60

continue_time = '{:02d}:{:02d}:{:02d}'.format(diff_h, diff_m, diff_s)

output_video_name = input_video_path.split('/')[-1].split('.')[0] + '_12' + '.mp4'
output_video_path = os.path.join(os.path.dirname(input_video_path), output_video_name)

command = [
    'ffmpeg',
    '-ss', start_time,
    '-t', continue_time,
    '-i', input_video_path,
    '-vcodec', 'copy',
    '-acodec', 'copy',
    output_video_path
]

p = sp.call(command)
