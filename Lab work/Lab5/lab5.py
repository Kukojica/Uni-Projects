import cv2
img = cv2.imread('Kojka.jpg')
scale_percent = 30  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
# 1.a
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh_img = cv2.threshold(gray_img, 130, 255, cv2.THRESH_BINARY)
cv2.imshow('Original image', img)
cv2.imshow('Grayscale image', gray_img)
cv2.imshow('Binary Thresholded image', thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 1.b
text = "Hehe or not Hehe"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
thickness = 2
color = (0, 255, 0)
text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
text_x = int((img.shape[1] - text_size[0]) / 2)
text_y = int((img.shape[0] - text_size[1]) / 2)
cv2.putText(img, text, (text_x, text_y), font, font_scale, color, thickness)
cv2.imshow('Image with text', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

start_x = 100
start_y = 100
end_x = 500
end_y = 500
cropped_image = img[start_y:end_y, start_x:end_x]
cv2.imshow('Cropped image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#1.c

angle = 90
rows, cols, _ = img.shape
rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
rotated_img = cv2.warpAffine(img, rotation_matrix, (cols, rows))
cv2.imshow('Rotated image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel_size = (5, 5)
blur_img = cv2.GaussianBlur(img, (51, 51), 0)
ksize = 11
sigma = 5
smooth_img = cv2.GaussianBlur(img, (ksize, ksize), sigma)
cv2.imshow('Blurred image', blur_img)
cv2.imshow('Smooth image', smooth_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#2
image = cv2.imread('people.jpg')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imshow('Image', image)
print('Number of faces detected:', len(faces))
cv2.waitKey(0)
cv2.destroyAllWindows()

#3
import numpy as np

def draw_circle(event,x,y,flags,param):
    if(event == cv2.EVENT_LBUTTONDBLCLK):
         cv2.circle(img,(x,y),100,(255,255, 0),-1)

def draw_free(event, x, y, flags, params):
    if event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_RBUTTON:
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

img = np.zeros((512, 512, 3), dtype=np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
cv2.setMouseCallback('image', draw_free)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

#4.a

capture = cv2.VideoCapture('IMG_0026.MOV')
framewidth = int(capture.get(3))
frameheight = int(capture.get(4))

x = int(framewidth / 4)
y = int(frameheight / 4)
width = int(framewidth / 2)
height = int(frameheight / 2)

while True:
    ret, frame = capture.read()
    if ret == True:
        croppedframe = frame[y:y + height, x:x + width]
        rotatedframe = cv2.rotate(croppedframe, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow('Rotated', rotatedframe)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

#4.b
capture.release()
cv2.destroyAllWindows()

capture = cv2.VideoCapture('IMG_0026.MOV')
framewidth = int(capture.get(3))
frameheight = int(capture.get(4))

x = int(framewidth / 4)
y = int(frameheight / 4)
width = int(framewidth / 2)
height = int(frameheight / 2)

while True:
    ret, frame = capture.read()
    if ret == True:
        croppedframe = frame[y:y + height, x:x + width]
        cv2.imshow('Original', frame)
        cv2.imshow('Cropped - RGB', croppedframe)
        grayframe = cv2.cvtColor(croppedframe, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Cropped - Gray', grayframe)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()

#4.c
capture = cv2.VideoCapture('vecteezy_beautiful-white-cherry-blossoms-at-riverside-in-japan_1626044.mp4')
framewidth = int(capture.get(3))
frameheight = int(capture.get(4))

newwidth = int(framewidth / 2)
newheight = int(frameheight / 2)

while True:
    ret, frame = capture.read()
    if ret == True:
        resizedframe = cv2.resize(frame, (newwidth, newheight))
        rotatedframe = cv2.rotate(resizedframe, cv2.ROTATE_180)
        cv2.imshow('Rotated', rotatedframe)
        blurredframe = cv2.GaussianBlur(rotatedframe, (7, 7), 0)
        cv2.imshow('Blurred', blurredframe)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()

#5

capture = cv2.VideoCapture('IMG_0026.MOV')
bgSubtractor = cv2.createBackgroundSubtractorMOG2()

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        fgMask = bgSubtractor.apply(frame)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        fgMask = cv2.morphologyEx(fgMask, cv2.MORPH_OPEN, kernel)
        contours, hierarchy = cv2.findContours(fgMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()