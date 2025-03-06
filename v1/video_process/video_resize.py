import cv2
import imageio
import os
from pathlib import Path


def video_resize(dir_path, dir_path_resize, fps, fourcc, new_size, video_format):
    video_files = os.listdir(dir_path)
    print(video_files)
    if "info.txt" in video_files:
        video_files.remove("info.txt")
    video_files.sort(key=lambda x: int(x.split('.')[0]))
    for video_name in video_files:
        if Path(video_name).suffix in video_format:
            print("========================================================")
            video_path = os.path.join(dir_path, video_name)
            print(video_path)
            store_path = os.path.join(dir_path_resize, video_name)
            print(store_path)
            writer = video_writer(store_path=store_path, fourcc=fourcc, fps=fps, size=new_size)
            cap, w, h, fps_orig, duration = video_reader(video_path=video_path)
            frame_counter = 0
            while True:
                ret, frame = cap.read()
                if ret:
                    frame_counter += 1
                    new_frame = cv2.resize(frame, new_size, interpolation=cv2.INTER_CUBIC)
                    # b, g, r = cv2.split(new_frame)
                    # new_frame = cv2.merge([r, g, b])
                    writer.write(frame[70:650, 0:1280])
                    # writer.write(new_frame)
                    print("\rvideo frames:{}".format(frame_counter), end="", flush=True)
                else:
                    print("\nThe End of Video {}".format(video_name))
                    writer.release()
                    break
    return print("Resize OK !")


def video_reader(video_path):
    capture = cv2.VideoCapture(video_path)
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = capture.get(cv2.CAP_PROP_FPS)
    if fps == 'inf':
        fps = 25
        duration = 0
    else:
        number_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = number_frames / fps / 60
    return capture, width, height, fps, duration


def video_reader_imageio(video_path):
    reader = imageio.get_reader(video_path)
    meta = reader.get_meta_data()
    width = meta['size'][0]
    height = meta['size'][1]
    fps = meta['fps']
    duration = meta['duration'] / 60
    return reader, width, height, fps, duration


def video_writer(store_path, fourcc, fps, size):
    new_writer = cv2.VideoWriter(store_path, fourcc, fps, size)
    return new_writer


def video_writer_imageio(store_path, fps):
    new_writer = imageio.get_writer(store_path, fps=fps)
    return new_writer


def save_video_info(dir_path, video_format):
    video_files = os.listdir(dir_path)
    if "info.txt" in video_files:
        video_files.remove("info.txt")
    video_files.sort(key=lambda x: int(x.split('.')[0]))
    with open(os.path.join(dir_path, "info.txt"), "w") as f:
        for video_name in video_files:
            if Path(video_name).suffix in video_format:
                video_path = os.path.join(dir_path, video_name)
                cap, w, h, fps, duration = video_reader_imageio(video_path=video_path)
                video_info = "Path:{}\tWidth:{}\tHeight:{}\tFPS:{}\tTime:{:.2f}".format(video_path, w, h, fps, duration)
                print(video_info)
                f.write(video_info)
                f.write("\n")
    return print("Info OK !")


if __name__ == '__main__':
    video_format = [".mp4", ".avi", ".mov"]
    dir_path = "/media/joshuawen/Data/video_det/exp/CenterNet_v2/video_original/7"
    dir_path_resize = "/media/joshuawen/Data/video_det/exp/CenterNet_v2/video_resize/7"
    dir_path_resize_2 = "/media/joshuawen/Data/video_det/exp/CenterNet_v2/video_resize_2/7"
    new_size = (1280, 580)
    fps = 25
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_resize(dir_path=dir_path_resize, dir_path_resize=dir_path_resize_2,
                 fps=fps, fourcc=fourcc, new_size=new_size, video_format=video_format)
    # save_video_info(dir_path=dir_path_resize, video_format=video_format)

