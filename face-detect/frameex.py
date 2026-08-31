# frame extracter

import cv2
import os
class extractor:
    def __init__(self,video):
        self.video_path = video

    def extract(self):
        output_path = "split_frames"
        os.makedirs(output_path, exist_ok=True)

        vid = cv2.VideoCapture(self.video_path)
        cv2.namedWindow("Test", cv2.WINDOW_NORMAL)
        fps = vid.get(cv2.CAP_PROP_FPS)
        if fps==0:
            fps=60
        
        delay = int(1000/fps)

        frame_id = 0

        while vid.isOpened():
            ret, frame = vid.read()
            if not ret:
                break

            cv2.imshow("Test", frame)
            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break

            cv2.imwrite(f"{output_path}/frame_{frame_id:05d}.jpg", frame)
            frame_id += 1
        vid.release()
        cv2.destroyWindow("Test")