::@ECHO OFF
SET url=%1
SET txt=%2
FOR /f "tokens=*" %%W in ('youtube-dl -g %url%') do ffmpeg -y -i %%W -vf "[0:v] scale=640:-2:flags=bicubic,drawtext=text='%txt%':fontfile='C\:/Windows/Fonts/impact.ttf':fontcolor=white:borderw=1:fontsize=18:alpha=0.67:x=(w-tw)/2:y=5,drawtext=text='\@tocamgar':fontfile='C\:/Windows/Fonts/arial.ttf':fontcolor=white:borderw=1:fontsize=18:alpha=0.67:x=w-tw-10:y=h-th-10" -map 0:v -map 0:a -crf 30 -ac 1 -q:a 1 "TWITTER-DL_360p_crf30_ac1.mp4"