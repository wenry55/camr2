gst-launch-1.0 -v v4l2src  device=/dev/video0 !video/x-raw,width=1920,height=1080,framerate=30/1 ! videoconvert ! videoscale! video/x-raw,width=640,height=480 ! mpph264enc! filesink location=a.mp4
