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
