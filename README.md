# Auto Video Labeling

Data is a huge factor in deep learning algorithms. The larger our data size, the better our model can generalize and learn.
However, data preparation is a very laborious and time-consuming process. That's why I wanted to develop an application that I thought would make this stage easier.
By using image processing techniques, it can track an object of your choice to a certain extent and saves the image and .txt file to the folder during tracking.
**Currently, it only works for one class and you can only label one object.**

**Note:** it does not work very stable in videos with multivariate background

### You can download the application using this link
[Download - auto_video_labeling.exe](https://drive.google.com/file/d/1t0bHjMo3m41nOevacauQEcUu33D3r9aU/view?usp=sharing) 

### 1. Open the application
![Alt text](https://github.com/MehmetOKUYAR/auto_label/blob/master/images/app.jpg?raw=true "App ico")

**You can also run it like this** `python main.py`


### 2. Fill in the relevant fields. If you leave it blank, the default values will be accepted.
![Alt text](https://github.com/MehmetOKUYAR/auto_label/blob/master/images/main_window.jpg?raw=true "main window")

**Load video path :** Specify the video path you want to label. If you leave it blank, your camera will open.

**Name start :** According to the entered number value, it saves the image and txt files by counting from that number. 
For example: *img1.jpg* and *img1.txt*

**Save per frame:** Saved to one file per frame based on the value entered

**Class Name :** Specifies the folder name and label name to be saved. **Note**: It cannot contain Turkish characters.

**Class Id :** label id must be entered




## Hotkeys
~~~~~~~
+--------------------+----------------------+
| s           | Create a rect box           |
+--------------------+----------------------+
| c           | Cancel selection rect box   |
+--------------------+----------------------+
| w           | reduces the window width    |
+--------------------+----------------------+
| e           | increases the window width  |
+--------------------+----------------------+
| a           | reduces window height       |
+--------------------+----------------------+
| z           | increases window height     |
+--------------------+----------------------+
| q           | close the video             |
+--------------------+----------------------+

~~~~~~~~~~~~~~~~~~~~~~~~~


## You can see how the program works in the gif below.

![into gif](https://github.com/MehmetOKUYAR/auto_label/blob/master/images/intro_fast.gif)

## Outputs
- **A folder is created according to the class name you entered.**

![Alt text](https://github.com/MehmetOKUYAR/auto_label/blob/master/images/default_label.jpg?raw=true "saved folder")

- **Labels and images are saved according to the beginning of the name you enter**

![Alt text](https://github.com/MehmetOKUYAR/auto_label/blob/master/images/deafult_name.jpg?raw=true "name images")

- **Labels are saved in Yolo format.**

![Alt text](https://github.com/MehmetOKUYAR/auto_label/blob/master/images/example_txt.jpg?raw=true "sexample_txt")

## Results
~~~~~~~
        def save_img_txt(image, box, count,H,W,class_id):

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
            
            yolo_data = [[class_id, x_center, y_center, w, h]]

            file_path = os.path.join(photo_dir, image_name + ".txt")

            with open(file_path, 'w') as f:
                np.savetxt(
                    f,
                    yolo_data,
                    fmt=["%d", "%f", "%f", "%f", "%f"]
                )
~~~~~~~~~~~~~~~~~~~~~~~~~                
                
