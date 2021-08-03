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

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      lmlist = []
      for hand_landmarks in results.multi_hand_landmarks:
        for id, lm in enumerate(hand_landmarks.landmark):
          # print(id, lm)
          h, w, c = image.shape
          cx, cy = int(lm.x * w), int(lm.y * h)
          lmlist.append([id, cx, cy])
          # print(len(lmlist))
        if len(lmlist) != 0:
          x1, y1 = lmlist[4][1], lmlist[4][2]
          x2, y2 = lmlist[8][1], lmlist[8][2]
          cv2.circle(image, (x1, y1), 18, (120, 0, 120), cv2.FILLED)
          cv2.circle(image, (x2, y2), 18, (120, 0, 120), cv2.FILLED)
          cv2.line(image, (x1, y1), (x2, y2), (120, 0, 120), 3)
          length = math.hypot(x2 - x1, y2 - y1)
          print(length)

          brightness = np.interp(length, [2, 250], [0, 100])
          brightness_bar = np.interp(length, [2, 250], [85, 50])
          print(int(length), brightness)
          sbc.set_brightness(brightness, display=0)
          print(sbc.get_brightness())
          cv2.rectangle(image, (150, 50), (400, 85), (131, 238, 255), 3)
          cv2.rectangle(image, (150, int(brightness_bar)), (400, 85), (131, 238, 255), cv2.FILLED)

        else:
          print('no fingertip')

    cv2.imshow('Turukka_Hand_Brightness_Control', image)
    #writer.write(image)
    if cv2.waitKey(5) == ord('q'):
      break

cap.release()
# writer.release()