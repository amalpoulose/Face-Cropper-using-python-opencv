# face-cropper

It is a program written in python to crop faces from photos saved in a directory.
It is developed in order to provide help for data entry or can be used for some other application.

It is coded in python 2.7 so it doesn't work for python 3 or above (https://www.python.org/download).

You have to install opencv for python, for installation better to refer on internet.

   Opencv python doc: https://readthedocs.org/projects/opencv-python-tutroals/downloads/pdf/latest/
   
   For Ubuntu users, you can check on this link to install opencv : https://help.ubuntu.com/community/OpenCV
                       or     simply use: 'sudo apt-get install python-opencv' on terminal
   

Using this program, we can crop all faces in one or more photos in a folder.

*- The photos we want to crop is first saved in a directory

*- While running the program, we have to enter the folder where photos are saved also another folder where we want to save our result, if folder is not present, it will create new one

*-The faces in each photo will saved in new folder with identifiable file name.

*- If no faces present or non cropable image it will be saved inside a folder called 'invalid' inside the new folder.

*-It will take only jpg or png files.
