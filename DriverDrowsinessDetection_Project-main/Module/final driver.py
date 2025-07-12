import time
import random
import cv2
import os
import numpy as np
from pygame import mixer
import matplotlib.pyplot as plt
from keras.models import load_model

class Vehicle:
    def __init__(self):
        self.speed = 0
        self.max_speed = 120
        self.min_speed = 0
        self.drowsiness_threshold = 30
        self.drowsy = False
        self.history = {'time': [], 'speed': []}

    def accelerate(self):
        if self.speed < self.max_speed:
            self.speed += random.randint(5, 15)
            if self.speed > self.max_speed:
                self.speed = self.max_speed

    def decelerate(self):
        if self.speed > self.min_speed:
            self.speed -= random.randint(5, 10)
            if self.speed < self.min_speed:
                self.speed = self.min_speed

    def update_history(self, time_elapsed):
        self.history['time'].append(time_elapsed)
        self.history['speed'].append(self.speed)

    def check_drowsiness(self, frame, font):
        plt.plot(self.history['time'], self.history['speed'])
        plt.xlabel('Time (seconds)')
        plt.ylabel('Speed (km/h)')
        plt.title('Vehicle Speed Over Time')
        plt.show()

def main():
    vehicle = Vehicle()
    start_time = time.time()

    mixer.init()
    sound = mixer.Sound(r'C:\Users\91931\OneDrive\Desktop\SHARDA\PBL 3\Drowsiness detection\Drowsiness detection\alarm.wav')

    face = cv2.CascadeClassifier('haar cascade files\haarcascade_frontalface_alt.xml')
    leye = cv2.CascadeClassifier('haar cascade files\haarcascade_lefteye_2splits.xml')
    reye = cv2.CascadeClassifier('haar cascade files\haarcascade_righteye_2splits.xml')
    model = load_model('models/cnncat2.h5')
    path = os.getcwd()
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    count = 0
    score = 0
    thicc = 2
    rpred = [99]
    lpred = [99]

    while True:
        elapsed_time = time.time() - start_time

        vehicle.accelerate()
        vehicle.update_history(elapsed_time)

        ret, frame = cap.read()
        if not ret:
            break

        vehicle.check_drowsiness(frame, font)

        if vehicle.drowsy:
            try:
                sound.play()
            except:
                pass
            if thicc < 16:
                thicc = thicc + 2
            else:
                thicc = thicc - 2
                if thicc < 2:
                    thicc = 2
            cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 255), thicc)

        cv2.imshow('frame', frame)

        if elapsed_time >= 60:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(1)

    vehicle.plot_speed()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
