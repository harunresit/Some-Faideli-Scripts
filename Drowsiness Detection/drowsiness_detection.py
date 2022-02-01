import cv2
import dlib
import imutils
from imutils import face_utils
import math

pi = 3.14
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

video_capture = cv2.VideoCapture(0)                                                                               

def distance(x1,y1,x2,y2):
   x_uzunluk = abs(x1-x2)
   y_uzunluk = abs(y1-y2)

   return (math.sqrt(x_uzunluk^2 + y_uzunluk^2))

while True:
   # Capture frame-by-frame
   ret, frame = video_capture.read()
   #ret2, frame2 = video_captur2.read()
   # detect faces in the grayscale image


   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
   rects = detector(gray, 1)

   for (i, rect) in enumerate(rects):
      # determine the facial landmarks for the face region, then
      # convert the facial landmark (x, y)-coordinates to a NumPy
      # array
      shape = predictor(gray, rect)
      shape = face_utils.shape_to_np(shape)
   
      # convert dlib's rectangle to a OpenCV-style bounding box
      # [i.e., (x, y, w, h)], then draw the face bounding box
      (x, y, w, h) = face_utils.rect_to_bb(rect)
      cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
   

      
      ear_sol = (distance(shape[37][0],shape[37][1],shape[41][0],shape[41][1]) + distance(shape[38][0],shape[38][1],shape[40][0],shape[40][1]))/(2*distance(shape[36][0],shape[36][1],shape[39][0],shape[39][1]))
      ear_sag = (distance(shape[43][0],shape[43][1],shape[47][0],shape[47][1]) + distance(shape[44][0],shape[44][1],shape[46][0],shape[46][1]))/(2*distance(shape[42][0],shape[42][1],shape[45][0],shape[45][1]))
      mar = (distance(shape[62][0],shape[62][1],shape[66][0],shape[66][1]))/(distance(shape[60][0],shape[60][1],shape[64][0],shape[64][1]))
      area = ((distance(shape[37][0],shape[37][1],shape[40][0],shape[40][1])/2)**2)*pi
      #ear_sol = (abs(shape[37][1]-shape[41][1]) + abs(shape[38][1]-shape[40][1]))/(2*abs(shape[36][0]-shape[39][0]))
      #ear_sag = (abs(shape[43][1]-shape[47][1]) + abs(shape[44][1]-shape[46][1]))/(2*abs(shape[42][0]-shape[45][0]))
      #mar = abs(shape[62][1]-shape[66][1])/abs(shape[60][0]-shape[64][0])

      #area = pi*((math.sqrt((shape[37][0]-shape[40][0])^2 + (shape[37][1]-shape[40][1])^2)/2)^2)
      perimeter = distance(shape[36][0],shape[36][1],shape[37][0],shape[37][1]) + distance(shape[37][0],shape[37][1],shape[38][0],shape[38][1]) + distance(shape[38][0],shape[38][1],shape[39][0],shape[39][1]) + distance(shape[39][0],shape[39][1],shape[40][0],shape[40][1]) + distance(shape[40][0],shape[40][1],shape[41][0],shape[41][1]) + distance(shape[41][0],shape[41][1],shape[36][0],shape[36][1])

      pug = (4*pi*area)/(perimeter**2)
      # loop over the (x, y)-coordinates for the facial landmarks
      # and draw them on the image
      moe = mar/((ear_sag + ear_sol)/2)
      print(moe)

      if(moe>1):
         # show the face number
         cv2.putText(frame, "Uykulu #{}".format(i + 1), (x - 10, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
      else:
         cv2.putText(frame, "Dinc #{}".format(i + 1), (x - 10, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
      for (x, y) in shape:
         cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

   cv2.imshow('Video', frame)
   key = cv2.waitKey(1) & 0xFF
   # if the `q` key was pressed, break from the loop
   if key == ord("q"):
      break