SET video=%1

ffmpeg ^
	-i %video% ^
  	-filter_complex ^"^
		[0:v]
			delogo=
				x=775:
				y=6:
				w=62:
				h=62
		[v]
	"^
	-map "[v]" ^
	-map 0:a ^
	-c:a aac ^
	-q:a 1 ^
	-ac 1 ^
	-c:v h264 ^
	-crf 30 ^
	%video%_delogo.mp4
