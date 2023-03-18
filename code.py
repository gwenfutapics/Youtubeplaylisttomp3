from moviepy.editor import *
from pytube import Playlist
import os
import tempfile

link = input("Please enter playlist link:")
try:
    yt_playlist = Playlist(link)
except:
    print("Invalid URL")
    exit()

download_directory = "D:/mp4"
output_directory = "D:/mp3"

if not os.path.exists(download_directory):
    os.makedirs(download_directory)

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

print("Downloading videos...")
with tempfile.TemporaryDirectory() as temp_dir:
    for video in yt_playlist.videos:
        try:
            video.streams.get_lowest_resolution().download(temp_dir)
            print(f"Video Downloaded: {video.title}")
            video_path = os.path.join(temp_dir, video.title + ".mp4")
            audio = VideoFileClip(video_path).audio
            output_path = os.path.join(output_directory, f"{video.title}.mp3")
            audio.write_audiofile(output_path)
            print(f"Audio Converted: {video.title}")
        except Exception as e:
            print(f"Error: {str(e)}\nSkipping video: {video.title}")
print("\nAll videos are downloaded and converted.")
