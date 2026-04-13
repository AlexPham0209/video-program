import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer
import time

# Constants
WIDTH, HEIGHT = 1080, 720
cap = None
player = None
finished = True

while True:     
    if cap:
        # 1. Grab the video frame
        ret, frame = cap.read()
        
        # 2. Grab the audio/sync info
        # val represents the delay needed to stay synced
        audio_frame, val = player.get_frame()

        if not ret:
            cap.release()
            finished = True
            cap = None
            continue 
        
        # 3. Handle EOF (End of File) from ffpyplayer
        if val == 'eof':
            cap.release()
            finished = True
            cap = None
            continue

        # 4. Display the frame
        cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Video",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Video", frame)

        # 5. THE SYNC STEP
        # If val is positive, we need to wait that long to stay in sync
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
        # Idle state (no video playing)\
        cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Video",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Video", np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8))

        key = cv2.waitKey(10)
        
        if finished:
            # Simple map for demonstration
            video_map = {ord('a'): "videos/a.mp4", ord('b'): "videos/b.mp4", ord('c'): "videos/c.mp4"}
            
            if key in video_map:
                cap = cv2.VideoCapture(video_map[key])
                player = MediaPlayer(video_map[key])
                finished = False
            elif key == ord('q'):
                break

cv2.destroyAllWindows()