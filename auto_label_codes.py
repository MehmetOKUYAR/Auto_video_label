from auto_label_python import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog,QMessageBox
from PyQt5.QtGui import QIntValidator

import cv2
import os
from pathlib import Path
import numpy as np
import sys
from datetime import datetime
import random


class auto_label(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.ui.lineEdit_name.setValidator(QIntValidator(0,100000000,self))
        self.ui.lineEdit_frame.setValidator(QIntValidator(0,100000000,self))
        self.ui.lineEdit_classId.setValidator(QIntValidator(0,100000000,self))
        self.ui.pushButton_loadVideo.clicked.connect(self.load_video)
        self.ui.pushButton_start.clicked.connect(self.start)
        self.fileName = 0

    def load_video(self):
        self.fileName = QFileDialog.getOpenFileName()[0]
        self.ui.pushButton_loadVideo.setText(self.fileName)
        
    def start(self):

        initBB = None

        vs = cv2.VideoCapture(self.fileName)

        if self.ui.lineEdit_classname.text() == '':
            class_name = 'label'
        else:    
            class_name = self.ui.lineEdit_classname.text()

        
        

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
            
     
        count = 0
        frame_count = 0
        
        try:
            per_frame = int(self.ui.lineEdit_frame.text())
        except:
            per_frame =1

        try:
            class_id = int(self.ui.lineEdit_classId.text())
        except:
           class_id =0 

        saved_image = 0
        if not vs.isOpened():
            QMessageBox.warning(self,'Warning Message',' The video could not be opened. Please check the file type ! ')
            self.load_video()
            
        else:   
            cv2.namedWindow('Frame',cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Frame',800,800) 
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
                        tracker = cv2.TrackerCSRT_create()
                        tracker.init(frame, initBB)
                    except:
                        pass


                    
                    # if the `q` key was pressed, break from the loop
                elif key == ord("q"):
                    break

       
        vs.release()
        # close all windows
        cv2.destroyAllWindows()
