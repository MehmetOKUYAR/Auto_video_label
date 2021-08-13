from auto_label_python import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QIntValidator

import cv2
import os
from pathlib import Path
import numpy as np


class auto_label(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit_name.setValidator(QIntValidator(0,100000000,self))
        self.ui.lineEdit_frame.setValidator(QIntValidator(0,100000000,self))

        self.ui.pushButton_loadVideo.clicked.connect(self.load_video)
        self.ui.pushButton_start.clicked.connect(self.start)

    def load_video(self):
        self.fileName = QFileDialog.getOpenFileName()[0]
        self.ui.pushButton_loadVideo.setText(self.fileName)

    def start(self):

        initBB = None

        vs = cv2.VideoCapture(self.fileName)

        photo_path = "30_limit"
        photo_dir = Path(photo_path)
        photo_dir.mkdir(parents=True, exist_ok=True)

        class_name = self.ui.lineEdit_classname.text()
        classes = os.path.join(photo_dir,"classes.txt")
        with open(classes, 'w') as f:
            f.write(class_name)

        def save_img_txt(image, box, count,H,W):

            image_name = f'img{count}'
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

            yolo_data = [[6, x_center, y_center, w, h]]

            file_path = os.path.join(photo_dir, image_name + ".txt")

            with open(file_path, 'w') as f:
                np.savetxt(
                    f,
                    yolo_data,
                    fmt=["%d", "%f", "%f", "%f", "%f"]
                )
            
        try :
            count = int(self.ui.lineEdit_name.text())
        except :
            count = 0

        frame_count = 0
        try:
            per_frame = int(self.ui.lineEdit_frame.text())
        except:
            per_frame =1

        saved_image = 0
        new_H = 1520
        new_W = 880
        while True:
            ret,frame = vs.read()
            if ret is None:
                break
            frame_count +=1
            image = frame.copy()
            
            frame = cv2.resize(frame,(new_H,new_W))
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
                        save_img_txt(image, box, count,H,W)

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
                    tracker = cv2.TrackerCSRT_create()
                    tracker.init(frame, initBB)
                except:
                    pass

            elif key == ord("a") :
                new_H += 50
            elif key == ord("z") :
                new_H -= 50


            elif key == ord("w") :
                new_W += 50
            elif key == ord("e") :
                new_W -= 50

                
                # if the `q` key was pressed, break from the loop
            elif key == ord("q"):
                break

       
        vs.release()
        # close all windows
        cv2.destroyAllWindows()
