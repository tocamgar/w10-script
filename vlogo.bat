@ECHO OFF
SET LOGO="E:\Pictures\logo-cam_53x26_50a.png"
SET VIDEO=%1
::ffmpeg -i %VIDEO% -i %LOGO% -filter_complex "overlay=439:242" -b:v 150k -c:a copy  %VIDEO:~0,-5%_logo.mp4"
ffmpeg -i %VIDEO% -i %LOGO% -filter_complex "overlay=x=(main_w-overlay_w-5):y=(main_h-overlay_h-5)" -q 1  %VIDEO:~0,-5%_logo.mp4"