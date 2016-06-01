import cv2
import re
import os
import commands

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

def validcheck(path):
    if not os.path.exists(path):
        print('path error!')
        return(0)


def crop(path_file,recp,recpy):
    img=cv2.imread(path_file,cv2.IMREAD_COLOR)

    gray = cv2.imread(path_file,cv2.IMREAD_GRAYSCALE)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    nig = 1
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), 2)

        colorr = cv2.imread(path_file, cv2.IMREAD_COLOR)
        crop_img = colorr[y - 50:y + h + 50, x - 50:x + w + 50]
        if nig > 1:
            v=recp+'-'+ str(nig-1) + '.jpg'
            cv2.imwrite(v, crop_img)
        else:
            v=recp  + '.jpg'
            cv2.imwrite(v, crop_img)
        nig = nig + 1
        if not os.path.getsize(v):
            os.remove(v)
    if nig == 1:

        commands.getoutput('cp '+path_file+' '+os.path.join(recpy,'invalid'))

def main():
    junk=0
    valid=0
    path=raw_input('enter the path to folder')
    recp=raw_input('enter the path to destination folder')
    if not os.path.exists(recp):
        k = os.mkdir(recp)
    k = os.path.join(recp, 'invalid')
    if not os.path.exists(k):
        k = os.mkdir(k)

    if not validcheck(path) and not validcheck(recp):
        data=os.listdir(path)

        for file in data:
            ext=re.findall(r'\.\w\w\w',file)[0]
            if ext=='.jpg' or ext =='.JPG' or ext == '.png':
                path_file=os.path.join(path,file)
                file_name=file.split(ext)[0]
                recp_file=os.path.join(recp,file_name)
                crop(path_file,recp_file,recp)
                valid +=1
            else:
                junk += 1
        print '\n\n\n\t\t  ' + str(valid) + ' valid files were converted and ' + str(junk) + ' files neglected'
    else:
        print '\n\n\n\t\t\t operation failed'

if __name__ == '__main__':
    main()
