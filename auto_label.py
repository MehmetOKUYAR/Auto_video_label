
import cv2
import os
from pathlib import Path
import numpy as np
import sys
from datetime import datetime
import random
import argparse

# requirements
# opencv-contrib-python==4.2.0.34

# Run
# python3 auto_label.py --video video.mp4 --classnName label --perFrame 5 --classId 0

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", type=str,
	help="path to input video file")
ap.add_argument("-n", "--className", type=str, default="label",
	help="Enter your class label name")
ap.add_argument("-p", "--perFrame", type=int, default=1,
	help="Enter your class label name")
ap.add_argument("-i", "--classId", type=int, default=0,
	help="Enter your class label name")
args = vars(ap.parse_args())


fileName = args["video"]
class_name = args["className"]
per_frame = args["perFrame"]
class_id = args["classId"]

count = 0
frame_count = 0
saved_image = 0
initBB = None

vs = cv2.VideoCapture(fileName)


photo_path = class_name
photo_dir = Path(photo_path)
photo_dir.mkdir(parents=True, exist_ok=True)


classes = os.path.join(photo_dir,"classes.txt")
with open(classes, 'w') as f:
    f.write(class_name)

def save_img_txt(image, box,H,W,class_id,name):
    ran_value = random.randrange(1,1000)
    image_name = f'{name}{ran_value}_' + datetime.now().strftime("%d.%m.%Y_%H.%M.%S") 
    cv2.imwrite(os.path.join(photo_dir, image_name + ".jpg"), image)

    height, width = image.shape[:2]

    (x1, y1, w1, h1) = [int(v) for v in box]

    x1 = (width*x1)/W
    y1 = (height*y1)/H
    w1 = (width*w1)/W
    h1 = (height*h1)/H
    x_center = ((x1+(((x1+w1)-x1)/2)))/width
    y_center = ((y1+(((y1+h1)-y1)/2)))/height
    w = w1/width
    h = h1/height
    
    yolo_data = [[class_id, x_center, y_center, w, h]]

    file_path = os.path.join(photo_dir, image_name + ".txt")

    with open(file_path, 'w') as f:
        np.savetxt(
            f,
            yolo_data,
            fmt=["%d", "%f", "%f", "%f", "%f"]
        )
    



if not vs.isOpened():
    print("video yüklenemedi")
   
    
else:    
    cv2.namedWindow('Frame',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Frame',800,800)
    tracker = cv2.TrackerCSRT_create()

    while True:
        ret,frame = vs.read()
        
        if ret is None:
            sys.exit()
            break
        frame_count +=1
        image = frame.copy()

        (H, W) = frame.shape[:2]
        
        
        if initBB is not None:
            
            (success, box) = tracker.update(frame)
            # check to see if the tracking was a success
            if success:
                # for box in boxes:
                (x, y, w, h) = [int(v) for v in box]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                if frame_count%per_frame == 0:
                    count += 1
                    saved_image +=1
                    save_img_txt(image, box,H,W,class_id,class_name)

            info = [
                ("Success", "Yes" if success else "No"),
                ("Saved images: ",f'{saved_image}')
            ]
    
            for (i, (k, v)) in enumerate(info):
                text = "{}: {}".format(k, v)
                cv2.putText(frame, text, (10, H - ((i * 20) + 20)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            
        
        
        
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the 's' key is selected, we are going to "select" a bounding
        # box to track
        if key == ord("s"):
            initBB = cv2.selectROI(
                "Frame", frame, fromCenter=False, showCrosshair=True)
            try:
                
                tracker.init(frame, initBB)
            except:
                pass

        elif key == ord("z") :
            initBB = None
 
            # if the `q` key was pressed, break from the loop
        elif key == ord("q"):
            break


vs.release()
# close all windows
cv2.destroyAllWindows()

