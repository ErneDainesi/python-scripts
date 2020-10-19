import pytube
import os


def get_url():
    return input("url: ")


def load_url(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    return video


def download_video(video):
    save_folder = "/home/erne/" + input("dir: ")
    while not os.path.exists(save_folder):
        save_folder = input("[INVALID_INPUT] dir: ")
    save_folder.rstrip("\n")
    print(f'Downloading "{video.title}"...')
    video.download(save_folder)
    print("Done!")


url = get_url()
video = load_url(url)
download_video(video)
