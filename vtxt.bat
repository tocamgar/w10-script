@ECHO OFF
SET VIDEO=%1
::ffmpeg -i %VIDEO% -vf drawtext="fontfile=C\\:/Windows/Fonts/impact.ttf:fontcolor=white:borderw=1:fontsize=24:alpha=0.67:x=(w-tw)/2:y=5:text='%2'" -b:v 150k -c:a copy %VIDEO:~0,-5%_txt.mp4"
ffmpeg -i %VIDEO% -vf drawtext="fontfile=C\\:/Windows/Fonts/impact.ttf:fontcolor=white:borderw=1:fontsize=18:alpha=0.67:x=(w-tw)/2:y=5:text=%2" -q 1 %VIDEO:~0,-5%_txt.mp4"
E:\V¡deos\MONARQUÖA\MENSAJE NAVIDAD