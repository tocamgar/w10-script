::SET VIDEO=%1
SET VIDEO="E:\V�deos\HUMOR\INTERMEDIO\VIDEOS MANIPULADOS MENSAJE DEL REY.mp4"
ffmpeg ^
-loglevel verbose ^
-i %VIDEO% ^
-vf ^
	scale="width=-2:height=360",drawtext="fontfile=C\\:/Windows/Fonts/arial.ttf:text=@tocamgar:fontcolor=white:borderw=1:fontsize=18:alpha=0.60:x=w-tw-10:y=h-th-10:expansion=none" ^
-map 0:v ^
-map 0:a? ^
-c:a aac ^
-q:a 1 ^
-ac 1 ^
-c:v h264 ^
-crf 30 ^
%VIDEO:~0,-5%_01.mp4"