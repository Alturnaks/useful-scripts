import moviepy.editor
from pathlib import Path

file = Path('video1.mp4')

video = moviepy.editor.VideoFileClip(f'{file}')
audio = video.audio
audio.write_audiofile(f'{file.stem}.mp3')