import cv2
import os

# Playing video from file:
cap = cv2.VideoCapture('videos/deep dream video.mp4')

try:
    if not os.path.exists('../data2'):
        os.makedirs('../data2')
except OSError:
    print ('Error: Creating directory of data')

success, image = cap.read()
count = 0
while success:
    success, frame = cap.read()
    name = '../data2/frame' + str(count) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)
    count += 1


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()