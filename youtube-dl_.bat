# https://forum.videohelp.com/threads/356314-How-to-batch-convert-multiplex-any-files-with-ffmpeg#post2243963

@echo off
:start
set /p YoutubeURL="Youtube URL: "
youtube-dl --ffmpeg-location "C:\ffmpeg\bin" --extract-audio --audio-quality 6 --audio-format mp3 --output "C:\SLAM\Songs\%%(title)s.%%(ext)s" %YoutubeURL%
GOTO :start