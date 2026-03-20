import cv2
import numpy as np

# Load the video file
cap = None
finished = True
WIDTH = 1080
HEIGHT = 720

# Read and display video frames
while True:    
    if cap:
        ret, frame = cap.read()

        if not ret:
            cap.release()
            finished = True
            cap = None
            continue 
        
        # frame = cv2.resize(frame, (WIDTH, HEIGHT)) 
        cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Video",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Video", frame)

    else:
        cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Video",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Video", np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8))
    
    key = cv2.waitKey(10)
    if finished:
        if key == ord('a'):
            cap = cv2.VideoCapture("videos/a.mp4")
        elif key == ord('b'):
            cap = cv2.VideoCapture("videos/b.mp4")
        elif key == ord('c'):
            cap = cv2.VideoCapture("videos/c.mp4")
        
        if key != -1:
            finished = False

    if key == ord('q'):
        break

cv2.destroyAllWindows()