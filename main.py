import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer
import time

# Load the video file
cap = None
player = None
finished = True
WIDTH = 1080
HEIGHT = 720

# Read and display video frames
while True:    
    if cap:
        ret, frame = cap.read()
        audio_frame, val = player.get_frame()

        if not ret or val == 'eof':
            cap.release()
            finished = True
            cap = None
            continue 
        
        # frame = cv2.resize(frame, (WIDTH, HEIGHT)) 
        cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Video",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Video", frame)

        if val > 0:
            # We wait for the time specified by ffpyplayer (converted to ms)
            # We subtract a tiny bit for processing overhead
            wait_time = int(val * 1000)
            if cv2.waitKey(wait_time) & 0xFF == ord('q'):
                break
        else:
            # If val is 0 or negative, we are lagging; skip the wait
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    else:
        cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Video",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Video", np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8))

        key = cv2.waitKey(10)
        if finished:
            if key == ord('a'):
                cap = cv2.VideoCapture("videos/e.mp4")
                player = MediaPlayer("videos/e.mp4")
            elif key == ord('b'):
                cap = cv2.VideoCapture("videos/b.mp4")
                player = MediaPlayer("videos/b.mp4")    
            elif key == ord('c'):
                cap = cv2.VideoCapture("videos/c.mp4")
                player = MediaPlayer("videos/c.mp4")
            
            if key != -1:
                finished = False

        if key == ord('q'):
            break

cv2.destroyAllWindows()
