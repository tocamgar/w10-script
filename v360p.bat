@ECHO OFF
SET VIDEO=%1
::SET TEXTO=%2
::SET TEXTO=%TEXTO:"='%
SET TEXTO='%~2'
::SET LOGO="E:\Pictures\logo-cam_53x26_50a.png"
::ffmpeg -i %VIDEO% -vf scale=288*a:288 -b:v 150k -b:a 56k %VIDEO:~0,-5%_288p_150k_56k.mp4"
::ff -y -i "https://vclip.antena3.com/vclip/_definst_/smil:assets11/2020/06/15/3167384A-E9FC-42DE-853A-72F0FF90325C/es.smil/chunklist_b578000.m3u8" -i "E:\Pictures\logo-cam_53x26_50a.png" -filter_complex "[0:v] scale=512:-2:flags=bicubic [v1];[v1][1:v]overlay=x=(main_w-overlay_w-5):y=(main_h-overlay_h-5),drawtext=fontfile='C\:/Windows/Fonts/impact.ttf':fontcolor=white:borderw=1:fontsize=18:alpha=0.67:x=(w-tw)/2:y=5:text='15-06-2020'" -b:v 150k -b:a 56k "PARADOJA RACISMO_150k_56k_txt_logo.mp4"
ffmpeg -y -i %VIDEO% -filter_complex "[0:v] scale=640:-2:flags=bicubic,drawtext=text='%TEXTO%':fontfile='C\:/Windows/Fonts/impact.ttf':fontcolor=white:borderw=1:fontsize=18:alpha=0.67:x=(w-tw)/2:y=5,drawtext=text='@tocamgar':fontfile='C\:/Windows/Fonts/arial.ttf':fontcolor=white:borderw=1:fontsize=18:alpha=0.67:x=w-tw-10:y=h-th-10" -crf 30 -ac 1 -q:a 1 %VIDEO:~0,-5%_360p_crf30_ac1.mp4"