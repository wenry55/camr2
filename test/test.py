import cv2

#pipeline = "v4l2src device=/dev/video0 ! video/x-raw,width=640,height=512,format=(string)I480,pixel-aspect-ratio=1/1,interlace-mode=(string)progressive, framerate=30/1 ! videoconvert ! appsink"
#pipeline = "v4l2src device=/dev/video0 !video/x-raw,framerate=20/1 ! videoscale! videoconvert ! appsink" 
#pipeline = "v4l2src !video/x-raw, width=1920,height=1080!queue ! mpph264enc ! rtph264pay name=pay0 pt=96"
pipeline = "rtspsrc location=rtsp://127.0.0.1:8554/test ! decodebin ! videoconvert ! appsink"
capture = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
#if not capture.isOpened():
#	print('video not opened.')
#	exit(0)

while True:
	ret, frame = capture.read()
	if not ret:
		print('failed.')
	else:
		print('success')

