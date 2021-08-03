import cv2
import mediapipe as mp
import math, numpy as np
import screen_brightness_control as sbc
import pyttsx3

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
drawing_styles = mp.solutions.drawing_styles

cap = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
#writer = cv2.VideoWriter('D:\zoom/tt.avi',cv2.VideoWriter_fourcc('X','V','I','D'), 30, (640,480))
engine = pyttsx3.init()
engine.say('Dear, Turukka, I am here')
engine.say('Turn on the webcam')
engine.runAndWait()


with mp_hands.Hands(
    min_detection_confidence = 0.7,
    min_tracking_confidence = 0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)